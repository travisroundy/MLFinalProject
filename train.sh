#train.sh
rm poke.model
rm train2.vw
sed 's/ *$//' train.vw > train2.vw
vw -f poke.model --passes=10 --learning_rate=0.2 --cache_file=poke.cache --kill_cache  --oaa 151 --predictions=predictions.txt --loss_function=hinge < train2.vw
