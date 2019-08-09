import gpt_2_simple as gpt2

def gpt_2():
    model_name = "117M"
    gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/117M/

    sess = gpt2.start_tf_sess()
    gpt2.finetune(sess,
                'titles.txt',
                model_name=model_name,
                steps=1000,
                save_every=200,
                sample_every=25)   # steps is max number of training steps

    gpt2.generate(sess)

if __name__ == "__main__":
    gpt_2()
