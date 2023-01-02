for i in {1..21}
do
   date | md5sum | tr -d '[:space:]-'
   echo
   sleep 1
done
