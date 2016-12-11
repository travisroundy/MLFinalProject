#train.sh
rm poke.model
rm train2.vw
sed 's/ *$//' train.vw > train2.vw
vw -f poke.model --passes=50 --learning_rate=0.2 --cache_file=poke.cache --kill_cache  --oaa 150 --predictions=predictions.txt --loss_function=logistic < train2.vw
