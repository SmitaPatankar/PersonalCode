# shells available on system
```
cat /etc/shells
```

# execute bash script by giving proper permissions
```
touch helloscript.sh
#! /bin/bash
# something
chmod +x helloscript.sh
./helloscript.sh
```

# redirect data to file
```
echo "hello bash scripting" > file.txt
cat > file.txt  
cat >> file.txt
```

# comments
```
# single line comment
:'multi
line comment'
```

# documentation
```
cat << document
sometext
document
```

# if, elif, else condition and comparison and logical operators
```
# -eq -ne -gt -lt -le -ge
# -a -o
count=10
if [ $count -lt 9 ] # if (( $count > 10 ))
then
    echo "first condition"
elif [ $count -le 9 ] && [ $count -gt 10 ]  # [[ $count -le 9 && $count -gt 10 ]] # [ $count -le 9 -a $count -gt 10 ]
then
    echo "second condition"
else
    echo "third condition"
fi
```

# case statement along with user input
```
echo "what is your age?"
echo "1 - 0-17"
echo "2 - 18-29"
echo "3 - 30 - 49"
echo "4 - 50-64"
read age;
case $age in
    1) echo "child"
    echo "play"
    ;;
    2) echo "adult";;
    3) echo "getting old";;
    4) echo "old";;
    *) echo "incorrect age";;
esac
```

# while loop
```
number=1
while [ $number -lt 10 ]
do
    echo "$number"
    number=$(( number+1 ))
done
```

# until loop
```
number=1
while [ $number -gt 10 ]
do
    echo "$number"
    number=$(( number+1 ))
done
```

# for loop, break and continue statement
```
for i in 1 2 3 4 5  # for i in {1..5}  # for i in {1..5..2}
do
    echo $i
done
```
```
for (( i=0; i<=5; i++ ))
do
    echo $i
done
```
```
for (( i=0; i<=5; i++ ))
do
    if [ $i -gt 5 ]
    then
        break
    fi
    echo $i
done
```
```
for (( i=0; i<=5; i++ ))
do
    if [ $i -eq 3 ]
    then
        continue
    fi
    echo $i
done
```

# script input from arguments and files
```
echo $0 $1 $2 $3

./script.sh smita neha pooja
```
```
args=("$@")  # args=("$3")
echo ${args[0]} ${args[1]} ${args[2]} ${args[3]}  # echo ${args[@]}
echo $#
```
```
while read line
do
    echo "$line"
done < "${1:-/dev/stdin}"

./script.sh
./script.sh my\ file
```

# script output as stdout and stderr
```
ls -al > stdout.txt
```
```
ls -al 1> stdout.txt 2>stderr.txt
```
```
ls -al > stdouterr.txt 2>&1  # ls -al >& stdouterr.txt
```

# send output from one script to another
```
touch 2.sh

echo "message from script 1 is: $msg"
```
```
touch 1.sh

msg="hello"
export msg

./2.sh
```

# string operations
```
echo "enter first string"
read st1
echo "enter second string"
read st2

c=$st1$st2
echo $c

echo ${st1^}
echo ${st1^^}
echo ${st1^l}

if [ $st1 == $st2 ]  # if [ $st1  \< $st2 ]
then
    echo "true"
else
    echo "false"
fi
```

# number operations
```
# + - / % *(\* in expr)

n1=4
n2=20
echo $(( n1+n2 ))  # echo $(expr $n1 + $n2)
```
```
echo "enter hex number"
read hex
echo -n "decimal of $hex is: "
echo "obase=10; ibase=16; $hex" | bc
```

# declare command for variables(read more about its significance)
```
declare -p
```
```
declare myvar
declare myvar=5
myvar=11
```
```
declare -r myvar=9
echo $myvar
```

# arrays
```
car=('a' 'b' 'c')

echo "${car[@]}"
echo "${car[0]}"

echo "${!car[0]}"
echo "${#car[@]}"

unset car[2]
car[2]="d"
```

# functions
```
function myfunc()
{
    echo "smita"
}

myfunc
```
```
function myfunc()
{
    echo $1 $2 $3 $4
}

myfunc hi i am smita
```
```
function myfunc()
{
    s="smita"
}

myfunc

echo $s
```

# files and directories(read more about IFS)
```
mkdir mydir
mkdir -p mydir

echo "enter dir name"
read direct
if [-d $direct ]
then
    echo "exists"
else
    echo "doesnt exist"
fi
```
```
echo "enter file name"
read f
if [ -f $f ]
then
    while IFS= read -r line
    do
        echo $line
    done < $f

    echo "enter text"
    read filetext
    echo $filetext >> $f
    
    rm $f
    echo "deleted"
else
    echo "doesnt exist"
fi
```

# send email
```
google account - allow less sure apps

sudo apt install ssmtp
vi /etc/ssmtp/ssmtp.conf
root=test@gmail.com
mailhub=smtp.gmail.com:587
AuthUser=test@gmail.com
AuthPass=xx
UseSTARTTLS=yes
```
```
ssmtp test@gmail.com

To: test@gmail.com
From: test@gmail.com
CC: test@gmail.com
Subject: test
Body: test
```

# curl
```
url="xx"

curl ${url} -O

curl ${url} -o myname.txt
curl ${url} > abc.txt

curl -I ${url}
```

# professional menus 
```
select car in a b
do
    case $car in 
    a)
        echo "a";;
    b)
        echo "b";;
    *)
        echo "wrong"
done
```
```
echo "press any key to continue"
while [ true ]
do
    read -t 3 -n 1
    if [ $? = 0 ]
    then
        echo "terminated"
        exit;
    else
        echo "waiting"
    fi
done
```

# wait for file system events with inotify
```
sudo apt install inotify-tools
```
```
inotifywait -m /temp/newfolder
```

# grep (read more about regex)
```
echo "enter filename"
read filename
if [ -f $filename ]
then
    echo "enter text to search"
    read pattern
    grep -i -n -v -c $pattern $filename
else
    echo "doesnt exist"
fi
```

# awk data manipulation (read more in detail)
```
echo "enter filename"
read filename
if [ -f $filename ]
then
    awk '{print}' $filename
    awk '/pattern/ {print}' $filename    
    awk '/pattern/ {print $3,$4}' $filename    
else
    echo "doesnt exist"
fi
```

# sed
```
echo "enter filename"
read filename
if [ -f $filename ]
then
    sed 's/i/I/g' $filename > newfile.txt  # sed -i 's/is/was/g' $filename
else
    echo "doesnt exist"
fi
```

# debugging bash script
```
bash -x ./script.sh

#! /bin/bash -x

set -x 
echo "xx"
set +x
echo "yy"
```