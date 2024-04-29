BEGIN {
  num_group_ops = 0
}

/pir-to-py-code group-ops begin/ {
  num_group_ops++
}

END {
  print(num_group_ops)
}
