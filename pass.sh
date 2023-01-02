for i in {1..10}
do
   tr -dc 'A-Za-z0-9!"#$%&'\''()+,-./:;=?@[\]^_`|~' </dev/urandom | head -c 13  ; echo
done
