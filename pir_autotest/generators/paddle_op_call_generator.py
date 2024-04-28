class PaddleOpCallGenerator:

  def __init__(self, module_name="paddle"):
    self.m = module_name

  def GenerateOpCall(self, op, *inputs):
    return getattr(self, op.GetPyVarName())(op, *inputs)

  def pd_op_subtract(self, op, x, y):
    return f"{x.name} - {y.name}"

  def cf_yield(self, op, *inputs):
    return "return " + ", ".join([input.name for input in inputs])

  def pd_op_exp(self, op, x):
    return f"{self.m}.exp({x.name})"

  def pd_op_full(self, op):
    return f"{self.m}.full(shape={op.attrs['shape']}, dtype='{op.attrs['dtype']}', fill_value={op.attrs['value']})"

  def builtin_shadow_output(self, op):
    return None

  def builtin_parameter(self, op):
    return None

  def pd_op_data(self, op):
    return None

  def pd_op_elementwise_pow(self, op, x, y):
    return f"{self.m}.pow({x.name}, {y.name})"

  def builtin_combine(self, op, *inputs):
    operands = ", ".join([input.name for input in inputs])
    return f"[{operands}]"

  def pd_op_concat(self, op, x, y):
    return f"{self.m}.concat({x.name}, {y.name})"

  def pd_op_sum(self, op, x, axis):
    return f"{self.m}.sum({x.name}, keepdim={op.attrs['keepdim']}, axis={axis.name})"

  def pd_op_matmul(self, op, x, y):
    return f"{self.m}.matmul({x.name}, {y.name}, transpose_x={op.attrs['transpose_x']}, transpose_y={op.attrs['transpose_y']})"

  def pd_op_split(self, op, x, y, z):
    return f"{self.m}.split({x.name}, {y.name}, {z.name})"

  def builtin_split(self, op, x):
    return f"{x.name}"

  def pd_op_full_int_array(self, op):
    values = ", ".join(map(str, op.attrs['value']))
    return f"[{values}]"

  def cinn_op_yield_store(self, op, x):
    return f"{x.name}"

  def cinn_op_concat(self, op, *inputs):
    operands = ", ".join([input.name for input in inputs])
    return f"{self.m}.concat([{operands}], axis={op.attrs['axis']})"

  def cinn_op_reduce_sum(self, op, x):
    return f"{self.m}.sum({x.name}, keepdim={op.attrs['keep_dim']}, axis={op.attrs['dim']})"

  def pd_op_sqrt(self, op, x):
    return f"{self.m}.sqrt({x.name})"

  def pd_op_transpose(self, op, x):
    return f"{self.m}.transpose({x.name}, perm={op.attrs['perm']})"

  def pd_op_add(self, op, x, y):
    return f"{x.name} + {y.name}"

  def pd_op_multiply(self, op, x, y):
    return f"{x.name} * {y.name}"

  def pd_op_divide(self, op, x, y):
    return f"{x.name} / {y.name}"

  def pd_op_greater_than(self, op, x, y):
    return f"{x.name} > {y.name}"

  def pd_op_less_than(self, op, x, y):
    return f"{x.name} < {y.name}"

  def pd_op_logical_and(self, op, x, y):
    return f"{self.m}.logical_and({x.name}, {y.name})"

  def cinn_op_scale(self, op, x):
    return f"{x.name} * {op.attrs['scale']} + {op.attrs['bias']}"

  def pd_op_cast(self, op, x):
    return f"{self.m}.cast({x.name}, dtype='{op.attrs['dtype']}')"

  def cinn_op_broadcast(self, op, x):
    return f"{self.m}.broadcast_to({x.name}, {op.attrs['out_shape']})"

  def cinn_op_reshape(self, op, x):
    return f"{self.m}.reshape({x.name}, {op.attrs['shape']})"
