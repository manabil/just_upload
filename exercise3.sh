cat user_emails.txt > user_emails.csv
echo "Slepp for 5 seconds"
sleep 5
chmod +x csv_to_html.py
echo "Slepp for 5 seconds"
sleep 5
chmod o+w /var/www/html
echo "Slepp for 5 seconds"
sleep 5
./csv_to_html.py user_emails.csv /var/www/html/user-emails.html
echo "Slepp for 5 seconds"
sleep 5
ls /var/www/html

