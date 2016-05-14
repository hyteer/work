REM 参考 http://www.cnblogs.com/zwq194/archive/2012/12/14/2817673.html
reg add HKLM\System\CurrentControlSet\Services\Tcpip\Parameters /f /v TcpTimedWaitDelay /t REG_DWORD /d 5
reg add HKLM\System\CurrentControlSet\Services\Tcpip\Parameters /f /v TcpNumConnections /t REG_DWORD /d 0x00fffffe
reg add HKLM\System\CurrentControlSet\Services\Tcpip\Parameters /f /v MaxUserPort /t REG_DWORD /d 65534
reg add HKLM\System\CurrentControlSet\Services\Tcpip\Parameters /f /v MaxFreeTcbs /t REG_DWORD /d 10000
reg add HKLM\System\CurrentControlSet\Services\Tcpip\Parameters /f /v MaxHashTableSize /t REG_DWORD /d 65536
reg add HKLM\System\CurrentControlSet\Services\Tcpip\Parameters /f /v EnableConnectionRateLimiting /t REG_DWORD /d 0