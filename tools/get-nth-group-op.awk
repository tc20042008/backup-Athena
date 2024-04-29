BEGIN {
  is_py_code = 0
  seq_no = 0
}

/pir-to-py-code group-ops end/ {
  is_py_code = 0
  seq_no++
}

/pir-to-py-code group-ops begin/ {
  is_py_code = 1;
}

{
  if (is_py_code == 1 && seq_no == group_idx) {
    print($0)
  }
}
