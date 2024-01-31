


class StorageExt:

	def __init__(self, owner):
		self.table_op = op("state_edit")
		self.owner = owner
		pass


	def Set(self, key, value):
		cell = self.table_op.cell(key, 1)
		# if there is an entry for this key
		if cell is not None:
			cell.val = value
		else:
			self.table_op.appendRow([key, value	])

	def Get(self, key):
		cell = self.table_op.cell(key, 1)
		if cell is not None:
			return cell.val
		op.log.Warning(f"Storage does not have key '{key}'")
		return None

	def Remove(self, key):
		if self.keyExists(key):
			self.table_op.deleteRow(key)
			return True
		op.log.Warning(f"'{key}' not found in storage, cannot remove it")
		return False

	def Reset(self):
		if len(self.owner.docked) == 1:
			op.log.Verbose("Reset storage to defaults")
			self.table_op.copy(self.owner.docked[0])
		

	def Clear(self):
		self.table_op.clear()


	def keyExists(key):
		return self.table_op[ key, 0 ] == key and not self.table_op[ key, 1 ] is None