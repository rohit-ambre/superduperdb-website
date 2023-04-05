collection.create_trainer('cgan_trainer', MyTrainer())
collection.create_learning_task('new_task', 'cgan_trainer', models=['generator', 'discrimator'],
                                keys=['input_1', 'input_2', ...])