#!/usr/bin/env bash
# 等 arxiv 单平台重跑结束后，自动启动过去几年（2021-01-01 .. 2025-09-08）全平台回填。
# 用法: nohup bash chain_backfill.sh > chain_backfill.log 2>&1 &
set -u

REPO="/data2/Daily-Paper-Agent-idp-interaction-ai"
cd "$REPO" || exit 1

PATTERN="scripts/backfill.py --since 2025-09-15 --until 2026-09-14 --platforms arxiv"

# 从正在跑的 arxiv 进程继承 env（本脚本可能运行在没有 ENTREZ_EMAIL/LLM_API_KEY 的新 shell 里）
ARXIV_PID=$(pgrep -f "$PATTERN" | head -1)
if [ -n "$ARXIV_PID" ] && [ -r "/proc/$ARXIV_PID/environ" ]; then
    while IFS= read -r -d '' var; do
        case "$var" in
            ENTREZ_EMAIL=*|LLM_API_KEY=*|LLM_BASE_URL=*|LLM_MODEL=*|NCBI_API_KEY=*|http_proxy=*|https_proxy=*|HTTP_PROXY=*|HTTPS_PROXY=*|no_proxy=*|NO_PROXY=*)
                export "$var"
                ;;
        esac
    done < "/proc/$ARXIV_PID/environ"
    echo "[$(date '+%F %T')] 已从 arxiv 进程 (pid=$ARXIV_PID) 继承 env"
else
    echo "[$(date '+%F %T')] 警告: 未找到 arxiv 进程或读不到 /proc environ，将依赖当前 shell 的 env"
fi

echo "[$(date '+%F %T')] 等待 arxiv 回填结束 (pattern: $PATTERN)"
while pgrep -f "$PATTERN" > /dev/null; do
    sleep 30
done
echo "[$(date '+%F %T')] arxiv 回填已结束"

echo "=== arxiv 缺 analysis.json（之后需补跑） ==="
for d in Archive/arxiv/*/*/*/; do
    [ ! -f "$d/analysis.json" ] && echo "  MISSING: $d"
done

echo "[$(date '+%F %T')] 启动过去几年回填: 2021-01-01 .. 2025-09-08"
exec python scripts/backfill.py --since 2021-01-01 --until 2025-09-08
