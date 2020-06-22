import time
import sys
sys.path.append(".")

from environment.BaseEnv import SumoBaseEnvironment
from environment.modules.CellsModule import CellsModule
from environment.modules.EmissionsModule import EmissionsModule, EmissionType
from environment.modules.EmissionsRendererModule import EmissionsRendererModule
from environment.modules.InductionLoopsModule import InductionLoopsModule

class CustomExperiment(SumoBaseEnvironment):
	def __init__(self, env_dir, out_dir=False, use_gui=False,num_seconds=20000):
		super().__init__(env_dir, out_dir, use_gui, num_seconds)


		cells 		= CellsModule(self._cell_shapes, self._edges_in_cells, self.cell_max_height, self.cell_max_width, self.cell_height, self.cell_width)
		emissions 	= EmissionsModule(cells, self.output_dir,[EmissionType.NOx], update_every=10, save_every=10, save_to_file=True)
		inductions 	= InductionLoopsModule(self.output_dir, self._induction_loops)
		#emissions_renderer = EmissionsRendererModule(emissions, [EmissionType.NOx], False)

		# Extra modules
		extra_modules = []
		extra_modules.append(cells)
		extra_modules.append(emissions)
		#extra_modules.append(emissions_renderer)
		extra_modules.append(inductions)

		self.set_extra_modules(extra_modules)


	def run(self):
		
		start = time.time()

		self.reset()
		while not self.is_done:
			print(self.sim_step)
			self.step()

		end = time.time()
		print("Took: ", end - start)

if __name__ == "__main__":
	if len(sys.argv) > 1:
		num_seconds = float(sys.argv[1]) #Expect number of seconds to simulate as argument
	else:
		num_seconds = 86400 #Simulate 1 day per default

	print(num_seconds)
		
		
	env = CustomExperiment(env_dir="simulations/small_extended/",out_dir="outputs/small_extended/",use_gui=False,num_seconds=num_seconds)
	env.run()
