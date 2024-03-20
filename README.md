# CANTONMT: Cantonese to English NMT Platform with Fine-Tuned Models using Real and Synthetic Back-Translation Data

Third Year Project for BSc Computer Science at the University of Manchester

## Introduction
This project focuses on developing models for translating Cantonese sentences to English sentences, where the trained models have obtained comparable results against State-of-the-Art commercial models (Bing, Baidu).

User Interface is provided to test out the models, and guides are provided below.


## Training
Datasets used for the training of models can be found on [Google Drive](https://drive.google.com/drive/folders/1fPvprgaZib-3LwvoXO__MeSo3VMErsor?usp=drive_link)

Training Files can also be found in the Notebooks folder.

## User Interface
To run the user interface for demonstration purposes, you should first download the model from [Google Drive](https://drive.google.com/drive/folders/1S53nHDP8Sc9n378-WilFB-yFOeGguFCl).  

The models should follow the same folder structure as in Google Drive under the Backend folder in the GitHub Repo.

Run the following code in the terminal to start the Backend

```bash
cd Backend
pip install -r requirement.txt
python app.py
```

To run the frontend user interface, run the following code in the terminal.

```bash
cd Frontend
npm i
npm run dev
```
The user interface should be correctly set up on http://localhost:3000/.

## Manchester NLP club talk
[recording-on-Youtube](https://youtu.be/KDdGua2wQOU)
[PPT](https://docs.google.com/presentation/d/1sp2Wn9t1zT-2DQFOpwlKyhiZCXnzC5tGqGfqQA9OuNY/edit?usp=drive_link  )
[demo-1min](https://youtu.be/s8P5fJjS7Ls?si=KWHOEfoOlAsDqa1l)

## Reference: Please cite our paper if you use the toolkit or data from this repository
[pre-print](https://github.com/kenrickkung/CantoneseTranslation/blob/main/view-CantonMT_v1.pdf)
'CANTONMT: Cantonese to English NMT Platform with Fine-Tuned Models using Synthetic Back-Translation Data'. 2024. 
Kung Yin Hong, Lifeng Han, Riza Batista-Navarro, Goran Nenadic. [Arxiv](https://arxiv.org/abs/2403.11346)

```latex
@misc{hong2024cantonmt,
      title={CantonMT: Cantonese to English NMT Platform with Fine-Tuned Models Using Synthetic Back-Translation Data}, 
      author={Kung Yin Hong and Lifeng Han and Riza Batista-Navarro and Goran Nenadic},
      year={2024},
      eprint={2403.11346},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```



