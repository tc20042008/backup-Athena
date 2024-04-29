num_group_ops=$(awk -f $(pwd)/get-num-fusion-ops.awk $1)

tmp_dir=$(mktemp -d)

for i in $(seq $num_group_ops)
do
  echo $i
  awk -v idx=$((i - 1)) -f $(pwd)/get-nth-fusion-op.awk $1 > $tmp_dir/program_$((i - 1)).py
done

echo $tmp_dir
