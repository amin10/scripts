diff $1 $2 &> /dev/null
if [ $? -eq 0 ]
then
    echo "removed"
    rm $1
fi
