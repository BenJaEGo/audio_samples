import wave
from glob import glob

import numpy as np

import csv


def check_identifiers(trial_filenames):
    identifiers = []
    for filename in trial_filenames:
        identifier = filename.split('/')[-1].split('.')[0]
        identifiers.append(identifier)

    print(set(identifiers))
    print(len(set(identifiers)))

    assert len(set(identifiers)) == len(trial_filenames)

    return identifiers


if __name__ == '__main__':

    dataset = "ljspeech"

    wav_filenames = glob(f'./*/{dataset}/*.wav')

    wav_filenames.sort()

    print(len(wav_filenames))

    num_methods = 8
    num_samples_each_method = 100

    diffwave = wav_filenames[0 * num_samples_each_method:1 * num_samples_each_method]
    fastdiff = wav_filenames[1 * num_samples_each_method:2 * num_samples_each_method]
    gt = wav_filenames[2 * num_samples_each_method:3 * num_samples_each_method]
    hifigan = wav_filenames[3 * num_samples_each_method:4 * num_samples_each_method]
    ours = wav_filenames[4 * num_samples_each_method:5 * num_samples_each_method]
    univnet = wav_filenames[5 * num_samples_each_method:6 * num_samples_each_method]
    waveglow = wav_filenames[6 * num_samples_each_method:7 * num_samples_each_method]
    wavegrad = wav_filenames[7 * num_samples_each_method:8 * num_samples_each_method]

    print(len(diffwave), len(fastdiff), len(gt), len(hifigan), len(ours), len(univnet), len(waveglow), len(wavegrad))

    # ours = wav_filenames[0:99]
    #
    print(wav_filenames[0], wav_filenames[99])
    print(wav_filenames[100], wav_filenames[199])
    print(wav_filenames[200], wav_filenames[299])
    print(wav_filenames[300], wav_filenames[399])
    print(wav_filenames[400], wav_filenames[499])
    print(wav_filenames[500], wav_filenames[599])
    print(wav_filenames[600], wav_filenames[699])
    print(wav_filenames[700], wav_filenames[799])
    #
    # print(len(wav_filenames))

    file_indexes = []
    for i in range(num_samples_each_method):
        file_indexes.append(np.random.permutation(num_methods))

    file_indexes = np.array(file_indexes)

    print(file_indexes.shape)

    trials = []
    for j in range(num_methods):
        trial = []
        current_file_indexes = file_indexes[:, j]
        for i in range(num_samples_each_method):
            if current_file_indexes[i] == 0:
                trial.append(diffwave[i])
            elif current_file_indexes[i] == 1:
                trial.append(fastdiff[i])
            elif current_file_indexes[i] == 2:
                trial.append(gt[i])
            elif current_file_indexes[i] == 3:
                trial.append(hifigan[i])
            elif current_file_indexes[i] == 4:
                trial.append(ours[i])
            elif current_file_indexes[i] == 5:
                trial.append(univnet[i])
            elif current_file_indexes[i] == 6:
                trial.append(waveglow[i])
            elif current_file_indexes[i] == 7:
                trial.append(wavegrad[i])
            else:
                raise ValueError(f'method index out of range.')

        print(len(trial))

        print(trial)

        check_identifiers(trial)

        trials.append(trial)

    print(len(trials))

    # trial_count = 1

    for trial_index in range(0, 8):
        trial = trials[trial_index]
        with open(f'trial{trial_index}.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['audio_url'])
            for sample in trial:
                print(sample)
                sample = "https://github.com/BenJaEGo/audio_samples" + sample[1:]
                writer.writerow([sample])
