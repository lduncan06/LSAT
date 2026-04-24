#!/bin/bash
cd /workspaces/LSAT

# Check Python syntax
python3 -c "import py_compile; py_compile.compile('lsat.py', doraise=True)" 2>&1 &
PID=$!
sleep 3
if kill -0 $PID 2>/dev/null; then
    echo "Compilation process still running - killing..."
    kill -9 $PID 2>/dev/null
    echo "Possible hanging/slow process"
fi
wait $PID 2>/dev/null
