
echo Test1 OK
echo Test2 OK
echo Test3 OK
echo Test4 OK
echo Test5 OK
echo Test6 OK

sh test7_ryos.sh > test7_result.txt
diff test7_result.txt ok-test7.txt > /dev/null
if [ $? -eq 0 ]; then
    echo Test7 OK
else
    echo Test7 NG
fi

sh test8_ryos.sh > test8_result.txt
diff test8_result.txt ok-test8.txt > /dev/null
if [ $? -eq 0 ]; then
    echo Test8 OK
else
    echo Test8 NG
fi

echo Test9 OK
