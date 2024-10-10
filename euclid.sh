echo -n 'input first number: '

read a

echo -n "input second number: "

read b

if [ $a -lt $b ]
then
	r0=$b
	r1=$a
	a=$r0
	b=$r1
else
	r0=$a
	r1=$b
fi

s0=1
s1=0
t0=0
t1=1

stemp=$s1
s1=$(($s0-$s1*($r0/$r1)))
s0=$stemp

ttemp=$t1
t1=$(($t0-$t1*($r0/$r1)))
t0=$ttemp
	
rtemp=$r1
r1=$(($r0 % $r1))
r0=$rtemp


while [ $r1 -gt 0 ]
do
	stemp=$s1
	s1=$(($s0-$s1*($r0/$r1)))
	s0=$stemp
	
	ttemp=$t1
	t1=$(($t0-$t1*($r0/$r1)))
	t0=$ttemp
	
	rtemp=$r1
	r1=$(($r0 % $r1))
	r0=$rtemp
done

echo "gcd($a,$b)=$r0"
echo "$s0*$a+$t0*$b=$r0"
echo "s=$s0"
echo "t=$t0"
