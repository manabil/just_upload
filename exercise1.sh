cat syslog.log
echo "Sleep for 5 seconds"
sleep 5
grep ticky syslog.log
echo "Sleep for 5 seconds"
sleep 5
grep "ERROR" syslog.log
echo "Sleep for 5 seconds"
sleep 5
grep "ERROR Tried to add information to closed ticket" syslog.log
echo "Sleep for 5 seconds"
sleep 5
./exercise1.py
