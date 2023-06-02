while IFS="," read -r name email
do
  echo "Name $name"
  echo "email: $email"
  
  python email_python.py $name $email
  
done <email_list.csv