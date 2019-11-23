# shell测试adb程序

function rand(){  
    min=$1  
    max=$(($2-$min+1))  
    num=$(($RANDOM+1000000000)) #增加一个10位的数再求余  
    echo $(($num%$max+$min))  
}  

while [ 1 -lt 10 ]
do
  adb shell input tap 300 2300
  sleep 1
  # adb shell input tap 100 1800
  # adb shell input text '顶贴'
  adb shell am broadcast -a ADB_INPUT_TEXT --es msg '今天'
  sleep 1
  adb shell input tap 1000 2250

  rnd=$(rand 500 1000)
  echo "$(date) sleep $rnd"
  sleep $rnd;
done
