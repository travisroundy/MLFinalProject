#test.sh
rm test2.vw
sed 's/ *$//' test.vw > test2.vw
vw -i poke.model -t -p ./predictions.txt < test2.vw
python accuracy.py
