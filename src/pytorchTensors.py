import torch

#getting the version of pytorch
print(torch.__version__)

#default data type in pytorch
print(torch.get_default_dtype())

#to change default datatype to torch float64
torch.set_default_dtype(torch.float64)

#default data type in pytorch
print(torch.get_default_dtype())

#lets create a new torch tensor
tensor_arr=torch.Tensor([[1,2,3],[4,5,6]])

#printing tensor
print(tensor_arr)



