# Thatcher Effect Dataset Generator

Using OpenCV to apply [Thatcher effect](https://en.wikipedia.org/wiki/Thatcher_effect) on [CelebA dataset](https://www.kaggle.com/jessicali9530/celeba-dataset)

## Example

### Input:

![input 1](https://user-images.githubusercontent.com/7780269/74758910-3d44b200-528d-11ea-858d-473e9eabfdf1.png)![input 2](https://user-images.githubusercontent.com/7780269/74758935-46ce1a00-528d-11ea-9820-905ac0d627cd.png)

### Output:

![output 1](https://user-images.githubusercontent.com/7780269/74758921-4170cf80-528d-11ea-99b3-a28f858442e1.png)![output 2](https://user-images.githubusercontent.com/7780269/74758946-49c90a80-528d-11ea-953b-70f4f64b4fa3.png)

## Run

1. Put the dataset CSV file beside the _main.py_ file (it's already there).
2. Put the dataset image files inside _input_images_ directory (some of them are already there).
3. You can change _main.py_ constants if you want.
4. Use Python 3 to run the program:

```bash
python main.py
```

It reads _input_files_ directory files and writes to _output_files_ directory.

## See Also

- [Large-scale CelebFaces Attributes (CelebA) Dataset](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html)
- [Thatcher Effect Illusion](http://thatchereffect.com/)
