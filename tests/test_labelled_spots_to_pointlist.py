import pyclesperanto_prototype as cle
import numpy as np

def test_labelled_spots_to_pointlist():

    gpu_input = cle.push(np.asarray([

            [0, 0, 0, 0, 0],
            [0, 1, 0, 3, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0],
            [0, 0, 0, 0, 4]

    ]))

    gpu_reference = cle.push(np.asarray([

            [1, 2, 3, 4],
            [1, 3, 1, 4]

    ]))



    gpu_output = cle.labelled_spots_to_pointlist(gpu_input)

    a = cle.pull(gpu_output)
    b = cle.pull(gpu_reference)

    print(a)
    print(b)

    assert (np.array_equal(a, b))
