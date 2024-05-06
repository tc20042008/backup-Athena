from pir_autotest.traits.args_trait import ArgsTrait
from pir_autotest.traits.type_trait import TypeTrait
from pir_autotest.traits.attr_trait import AttrTrait
from pir_autotest.traits.op_trait import OpTrait
from pir_autotest.generators.group_op_unittest_generator import GroupOpUnittestGenerator
from pir_autotest.apps import load_pir_py_classes
import sys


if __name__ == "__main__":
  for cls in load_pir_py_classes.GetProgramClasses(sys.argv[1]):
    ir_program = cls()
    generator = GroupOpUnittestGenerator()
    op_name2unittest = generator.Generate(ir_program)
    for name, unittest in op_name2unittest.items():
      print("#", "="*80)
      print("# file-splitter-fusion-op-name: ", name)
      print("#", "-"*80)
      print(unittest)