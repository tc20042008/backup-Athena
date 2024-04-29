num_group_ops=$(awk -f $(pwd)/get-num-group-ops.awk $1)

tmp_dir=$(mktemp -d)

touch $tmp_dir/__init__.py

for i in $(seq $num_group_ops)
do
  awk -v idx=$((i - 1)) -f $(pwd)/get-nth-group-op.awk $1 > $tmp_dir/program_$i.py
done

echo $tmp_dir
