from pir_autotest.generators.fusion_op_unittest_generator import (
  FusionOpUnittestGenerator
)
from pir_autotest.apps import load_pir_py_classes
import sys


if __name__ == "__main__":
  for cls in load_pir_py_classes.GetProgramClasses(sys.argv[1]):
    ir_program = cls()
    generator = FusionOpUnittestGenerator()
    op_name2unittest = generator.Generate(ir_program)
    for name, unittest in op_name2unittest.items():
      print("#", "="*80)
      print("# file-splitter-fusion-op-name: ", name)
      print("#", "-"*80)
      print(unittest)