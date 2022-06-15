dataset_info = dict(
    dataset_name='ap10k_mpii',
    paper_info=dict(
        author='Yu, Hang and Xu, Yufei and Zhang, Jing and '
        'Zhao, Wei and Guan, Ziyu and Tao, Dacheng',
        title='AP-10K: A Benchmark for Animal Pose Estimation in the Wild',
        container='35th Conference on Neural Information Processing Systems '
        '(NeurIPS 2021) Track on Datasets and Bench-marks.',
        year='2021',
        homepage='https://github.com/AlexTheBad/AP-10K',
    ),
    keypoint_info={
        0:
        dict(name='neck', id=0, color=[51, 153, 255], type='upper', swap=''),
        1:
        dict(
            name='pelvis',
            id=1,
            color=[51, 153, 255],
            type='lower',
            swap=''),
        2:
        dict(
            name='left_shoulder',
            id=2,
            color=[51, 153, 255],
            type='upper',
            swap='right_shoulder'),
        3:
        dict(
            name='left_elbow',
            id=3,
            color=[51, 153, 255],
            type='upper',
            swap='right_elbow'),
        4:
        dict(
            name='left_front_paw',
            id=4,
            color=[51, 153, 255],
            type='upper',
            swap='right_front_paw'),
        5:
        dict(
            name='right_shoulder',
            id=5,
            color=[0, 255, 0],
            type='upper',
            swap='left_shoulder'),
        6:
        dict(
            name='right_elbow',
            id=6,
            color=[255, 128, 0],
            type='upper',
            swap='left_elbow'),
        7:
        dict(
            name='right_front_paw',
            id=7,
            color=[0, 255, 0],
            type='upper',
            swap='left_front_paw'),
        8:
        dict(
            name='left_hip',
            id=8,
            color=[255, 128, 0],
            type='lower',
            swap='right_hip'),
        9:
        dict(
            name='left_knee',
            id=9,
            color=[0, 255, 0],
            type='lower',
            swap='right_knee'),
        10:
        dict(
            name='left_back_paw',
            id=10,
            color=[255, 128, 0],
            type='lower',
            swap='right_back_paw'),
        11:
        dict(
            name='right_hip',
            id=11,
            color=[0, 255, 0],
            type='lower',
            swap='left_hip'),
        12:
        dict(
            name='right_knee',
            id=12,
            color=[255, 128, 0],
            type='lower',
            swap='left_knee'),
        13:
        dict(
            name='right_back_paw',
            id=13,
            color=[0, 255, 0],
            type='lower',
            swap='left_back_paw')
    },
    skeleton_info={
        0:
        dict(link=('left_back_paw', 'left_knee'), id=0, color=[0, 255, 0]),
        1:
        dict(link=('left_knee', 'left_hip'), id=1, color=[0, 255, 0]),
        2:
        dict(link=('right_back_paw', 'right_knee'), id=2, color=[255, 128, 0]),
        3:
        dict(link=('right_knee', 'right_hip'), id=3, color=[255, 128, 0]),
        4:
        dict(link=('left_hip', 'right_hip'), id=4, color=[51, 153, 255]),
        5:
        dict(link=('left_shoulder', 'left_hip'), id=5, color=[51, 153, 255]),
        6:
        dict(link=('right_shoulder', 'right_hip'), id=6, color=[51, 153, 255]),
        7:
        dict(link=('left_shoulder', 'right_shoulder'), id=7, color=[51, 153, 255]),
        8:
        dict(link=('left_shoulder', 'left_elbow'), id=8, color=[0, 255, 0]),
        9:
        dict(link=('right_shoulder', 'right_elbow'), id=9, color=[255, 128, 0]),
        10:
        dict(link=('left_elbow', 'left_front_paw'), id=10, color=[0, 255, 0]),
        11:
        dict(link=('right_elbow', 'right_front_paw'), id=11, color=[255, 128, 0]),
        12:
        dict(link=('neck', 'right_shoulder'), id=12, color=[0, 128, 0]),
        13:
        dict(link=('neck', 'left_shoulder'), id=13, color=[0, 128, 0]),
        14:
        dict(link=('pelvis', 'right_hip'), id=14, color=[0, 128, 255]),
        15:
        dict(link=('pelvis', 'left_hip'), id=15, color=[0, 128, 255]),
        16:
        dict(link=('pelvis', 'neck'), id=16, color=[128, 128, 128]),
    },
    joint_weights=[
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.
    ],
    sigmas=[
        0.035, 0.035, 0.079, 0.072, 0.062, 0.079, 0.072, 0.062, 0.107, 0.087, 0.089, 0.107, 0.087, 0.089
    ])
