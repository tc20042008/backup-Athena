BEGIN {
  num_fusion_ops = 0
}

/pir-to-py-code fusion-ops begin/ {
  num_fusion_ops++
}

END {
  print(num_fusion_ops)
}
