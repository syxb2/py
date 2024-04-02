import paddle
import paddlehub as hub

paddle.enable_static()

# ---------------------------------------------------------- #

# 选择模型
# 此处代码为加载 Hub 提供的图像分类的预训练模型
module = hub.Module(name="xception71_imagenet")

# ---------------------------------------------------------- #

import os

path = "/home/aistudio/dog10"
folders_name = os.listdir(
    path
)  # os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。
print(folders_name)
if ".DS_Store" in folders_name:
    folders_name.remove(".DS_Store")
if ".ipynb_checkpoints" in folders_name:
    folders_name.remove(".ipynb_checkpoints")

for file in folders_name:
    print(file)

a = open("/home/aistudio/data/train_list.txt", "w")
b = open("/home/aistudio/data/validate_list.txt", "w")

count = 0
val_count = 0
train_count = 0

for name in folders_name:
    image_names = os.listdir(path + "/" + name)
    for img_name in image_names:
        if img_name != ".DS_Store":
            if count % 8 == 0:
                b.write(
                    path
                    + "/"
                    + name
                    + "/"
                    + img_name
                    + " "
                    + (str(int(name.split("-")[0]) - 1))
                    + "\n"
                )
                val_count = val_count + 1
            else:
                a.write(
                    path
                    + "/"
                    + name
                    + "/"
                    + img_name
                    + " "
                    + (str(int(name.split("-")[0]) - 1))
                    + "\n"
                )
                train_count = train_count + 1
        count = count + 1

a.close()
b.close()
print("train_list生成完毕，train数据集共{}个数据".format(train_count))
print("val_list生成完毕，val数据集共{}个数据".format(val_count))
print("合计{}个数据".format(count))

# ---------------------------------------------------------- #

d = open("/home/aistudio/data/label_list.txt", "w")

count = 0
label_count = 0

for name in folders_name:
    d.write(name + "\n")
    label_count = label_count + 1
    count = count + 1

d.close()
print("label_list生成完毕，label数据集共{}个数据".format(label_count))
print("合计{}个数据".format(count))

# ---------------------------------------------------------- #

c = open("/home/aistudio/data/test_list.txt", "w")

count = 0
test_count = 0

for name in folders_name:
    image_names = os.listdir(path + "/" + name)
    for img_name in image_names:
        if img_name != ".DS_Store":
            c.write(
                path
                + "/"
                + name
                + "/"
                + img_name
                + " "
                + (str(int(name.split("-")[0]) - 1))
                + "\n"
            )
            test_count = test_count + 1
        count = count + 1

c.close()
print("test_list生成完毕，test数据集共{}个数据".format(test_count))
print("合计{}个数据".format(count))

# ---------------------------------------------------------- #

from paddlehub.dataset.base_cv_dataset import BaseCVDataset


class DemoDataset(BaseCVDataset):
    def __init__(self):
        # 数据集存放位置
        self.dataset_dir = "/home/aistudio/data"
        super(DemoDataset, self).__init__(
            base_path=self.dataset_dir,
            train_list_file="train_list.txt",
            validate_list_file="validate_list.txt",
            test_list_file="test_list.txt",
            # predict_file="predict_list.txt",
            label_list=[
                "1-Basset Hound",
                "2-Beagle",
                "3-Gray hound",
                "4-German Shepherd",
                "5-Schnauzer",
                "6-Springer Spaniel",
                "7-Labrador",
                "8-Coker",
                "9-Oldenglishsheepdog",
                "10-Shetlan",
            ],
        )


# ---------------------------------------------------------- #

data_reader = hub.reader.ImageClassificationReader(
    image_width=module.get_expected_image_width(),  # 预期图片经过reader处理后的图像宽度
    image_height=module.get_expected_image_height(),  # 预期图片经过reader处理后的图像高度
    images_mean=module.get_pretrained_images_mean(),  # 进行图片标准化处理时所减均值。默认为None
    images_std=module.get_pretrained_images_std(),  # 进行图片标准化处理时所除标准差。默认为None
    dataset=dataset,
)

# ---------------------------------------------------------- #

config = hub.RunConfig(
    use_cuda=True,  # 是否使用GPU训练，默认为False；
    num_epoch=3,  # Fine-tune的轮数；使用4轮，直到训练准确率达到90%多
    checkpoint_dir="cv_finetune_turtorial_demo",  # 模型checkpoint保存路径, 若用户没有指定，程序会自动生成；
    batch_size=32,  # 训练的批大小，如果使用GPU，请根据实际情况调整batch_size；
    eval_interval=50,  # 模型评估的间隔，默认每100个step评估一次验证集；
    strategy=hub.finetune.strategy.DefaultFinetuneStrategy(),  # Fine-tune优化策略；
)

# ---------------------------------------------------------- #

# 获取 module 的上下文信息包括输入、输出变量以及 paddle program
input_dict, output_dict, program = module.context(trainable=True)

# 待传入图片格式
img = input_dict["image"]

# 从预训练模型的输出变量中找到最后一层特征图，提取最后一层的feature_map
feature_map = output_dict["feature_map"]

# 待传入的变量名字列表
feed_list = [img.name]

task = hub.ImageClassifierTask(
    data_reader=data_reader,  # 提供数据的 Reader
    feed_list=feed_list,  # 待 feed 变量的名字列表
    feature=feature_map,  # 输入的特征矩阵
    num_classes=dataset.num_labels,  # 分类任务的类别数量，此处来自于数据集的 num_labels
    config=config,  # 运行配置
)

# ---------------------------------------------------------- #

run_states = (
    task.finetune_and_eval()
)  # 通过众多 finetune API 中的 finetune_and_eval 接口，可以一边训练网络，一边打印结果

# ---------------------------------------------------------- #

import numpy as np

data = [
    "/home/aistudio/test-dog10/3-gray hound-test/2.jpg"
]  # 此处传入需要识别的照片地址
label_map = dataset.label_dict()
index = 0

# get classification result
run_states = task.predict(data=data)  # 进行预测
results = [
    run_state.run_results for run_state in run_states
]  # 得到用新模型预测test照片的结果

for batch_result in results:
    # get predict index
    batch_result = np.argmax(batch_result, axis=2)[0]
    for result in batch_result:
        index += 1
        result = label_map[result]
        print(
            "input %i is %s, and the predict result is %s"
            % (index, data[index - 1], result)
        )

# ---------------------------------------------------------- #
