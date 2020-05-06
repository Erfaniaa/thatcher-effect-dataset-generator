# Thatcher Effect Dataset Generator

Using OpenCV to apply [Thatcher effect](https://en.wikipedia.org/wiki/Thatcher_effect) on a set of face images

## Example

### Input:

![input 1](https://user-images.githubusercontent.com/7780269/74758910-3d44b200-528d-11ea-858d-473e9eabfdf1.png)![input 2](https://user-images.githubusercontent.com/7780269/74758935-46ce1a00-528d-11ea-9820-905ac0d627cd.png)

### Output:

![output 1](https://user-images.githubusercontent.com/7780269/81139360-b6919e00-8f7a-11ea-9e07-2acd7acbf30c.jpg)![output 2](https://user-images.githubusercontent.com/7780269/81139362-b85b6180-8f7a-11ea-9ae0-51e842e598a5.jpg)

Turn the output images upside-down to notice changes.

## Run

1. Put some image files inside _input_images_ directory (some samples from [CelebA dataset](https://www.kaggle.com/jessicali9530/celeba-dataset) are already there).
2. You can change _main.py_ constants if you want.
3. Use Python 3 to run the program:

```bash
python3 main.py
```

It reads _input_files_ directory files and writes to _output_files_ directory.

## See Also

- [Large-scale CelebFaces Attributes (CelebA) Dataset](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html)
- [Thatcher Effect Illusion](http://thatchereffect.com/)
