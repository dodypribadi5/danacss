from aim import Run


run = Run()

run['hparams'] = {
    'learning_rate': 0.001,
    'batch_size': 32,
}

for i in range(10):
    run.track(i, name='numbers')
