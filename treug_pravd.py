import matplotlib.pyplot as plt
import numpy as np


def func_pravda(theta,a):
    s=1
    for x in a:
        if x>=0 and x<=theta:
            s*=2*x/theta
        if x>theta and x<=1:
            s*=2*(1-x)/(1-theta)
    return s
vyborka=[0.3767, 0.1966, 0.3121, 0.7045, 0.7305, 0.4017, 0.7085, 0.4658, 0.485, 0.3997, 0.1392, 0.5105, 0.5656, 0.2939, 0.7918, 0.5516, 0.3113, 0.3207, 0.4633, 0.1943, 0.7025, 0.353, 0.7738, 0.8754, 0.4137, 0.5136, 0.2129, 0.2724, 0.078, 0.5, 0.1183, 0.4748, 0.41, 0.5034, 0.1151, 0.4103, 0.2355, 0.3603, 0.6214, 0.6396, 0.2161, 0.6311, 0.3457, 0.3009, 0.4232, 0.635, 0.4301, 0.2051, 0.3407, 0.6528, 0.2937, 0.5388, 0.7953, 0.6021, 0.671, 0.288, 0.2176, 0.0528, 0.4642, 0.2871, 0.3972, 0.7271, 0.4867, 0.098, 0.5038, 0.7432, 0.3213, 0.3887, 0.2988, 0.2356, 0.4293, 0.4548, 0.8434, 0.6933, 0.7586, 0.4894, 0.3207, 0.3984, 0.4177, 0.4678, 0.5981, 0.5973, 0.502, 0.7342, 0.4067, 0.409, 0.6955, 0.2232, 0.7358, 0.456, 0.5798, 0.5778, 0.6262, 0.1977, 0.4745, 0.5249, 0.6172, 0.7727, 0.3799, 0.4515, 0.3097, 0.0828, 0.4432, 0.3868, 0.7981, 0.3664, 0.6379, 0.534, 0.6291, 0.1643, 0.1275, 0.0972, 0.2671, 0.5188, 0.4219, 0.4583, 0.2838, 0.5559, 0.3158, 0.6619, 0.1883, 0.671, 0.2054, 0.4449, 0.3516, 0.4563, 0.0752, 0.2255, 0.6166, 0.5414, 0.5954, 0.5605, 0.3574, 0.3288, 0.8646, 0.1466, 0.2603, 0.3823, 0.4278, 0.3089, 0.7321, 0.3229, 0.3967, 0.7582, 0.3836, 0.2693, 0.6044, 0.4242, 0.6393, 0.5648, 0.4474, 0.3799, 0.3784, 0.9699, 0.5289, 0.4326, 0.7551, 0.6382, 0.3558, 0.5083, 0.3318, 0.5695, 0.8538, 0.478, 0.3745, 0.206, 0.1385, 0.7581, 0.5771, 0.027, 0.2185, 0.5584, 0.5993, 0.4369, 0.2315, 0.323, 0.5932, 0.597, 0.5727, 0.5735, 0.6829, 0.2455, 0.7825, 0.1509, 0.4778, 0.4686, 0.6086, 0.3512, 0.2414, 0.2922, 0.3881, 0.2371, 0.579, 0.8023, 0.4048, 0.306, 0.8046, 0.2028, 0.4355, 0.4859, 0.8144, 0.2782, 0.3751, 0.4941, 0.4266, 0.3301, 0.2815, 0.5446, 0.6596, 0.538, 0.3148, 0.1606, 0.2769, 0.8194, 0.5258, 0.2964, 0.3257, 0.7214, 0.773, 0.3747, 0.1298, 0.8677, 0.8628, 0.8412, 0.3766, 0.5233, 0.4157, 0.3998, 0.085, 0.1726, 0.8627, 0.2716, 0.5692, 0.3005, 0.2943, 0.4271, 0.4249, 0.1688, 0.5668, 0.1583, 0.4072, 0.4675, 0.7262, 0.4896, 0.4323, 0.2464, 0.2186, 0.7463, 0.4315, 0.1812, 0.7381, 0.4603, 0.392, 0.3007, 0.4805, 0.8243, 0.4575, 0.1454, 0.3714, 0.9298, 0.8743, 0.2939, 0.3484, 0.4142, 0.5162, 0.7214, 0.4557, 0.2919, 0.6128, 0.4295, 0.1313, 0.5392, 0.4091, 0.675, 0.8233, 0.6225, 0.8878, 0.6407, 0.5048, 0.657, 0.0283, 0.5049, 0.1975, 0.5787, 0.5461, 0.9833, 0.6119, 0.8439, 0.525, 0.3875, 0.3528, 0.4196, 0.3628, 0.349, 0.3639, 0.4438, 0.1938, 0.1684, 0.0904, 0.5709, 0.5856, 0.6748, 0.3799, 0.2412, 0.6831, 0.3514, 0.2531, 0.1587, 0.5493, 0.7873, 0.6153, 0.9118, 0.5779, 0.4222, 0.3011, 0.3196, 0.368, 0.5862, 0.4503, 0.7518, 0.9364, 0.3979, 0.1277, 0.4174, 0.6821, 0.4646, 0.8864, 0.7759, 0.3279, 0.5881, 0.6322, 0.0166, 0.4353, 0.3775, 0.2865, 0.3269, 0.3928, 0.4167, 0.4026, 0.028, 0.3496, 0.5334, 0.2169, 0.353, 0.3114, 0.5821, 0.7007, 0.2377, 0.4667, 0.312, 0.2935, 0.4511, 0.3632, 0.3488, 0.4479, 0.3715, 0.3859, 0.6054, 0.3634, 0.3262, 0.7175, 0.6605, 0.2984, 0.4491, 0.4503, 0.197, 0.2476, 0.3723, 0.2721, 0.3922, 0.4484, 0.3073, 0.3846, 0.5335, 0.0921, 0.5779, 0.4187, 0.268, 0.8386, 0.468, 0.8733, 0.1491, 0.4101, 0.3482, 0.7576, 0.693, 0.2212, 0.2679, 0.1938, 0.4515, 0.3339, 0.5136, 0.376, 0.4027, 0.104, 0.5727, 0.6503, 0.3349, 0.4698, 0.0176, 0.6971, 0.7418, 0.4586, 0.1743, 0.2526, 0.2219, 0.3399, 0.5805, 0.5398, 0.7606, 0.2893, 0.5269, 0.276, 0.5875, 0.3907, 0.2756, 0.7592, 0.7851, 0.6059, 0.6578, 0.5305, 0.2159, 0.5068, 0.5161, 0.2309, 0.4258, 0.8845, 0.2925, 0.4994, 0.4299, 0.237, 0.1386, 0.6275, 0.4434, 0.5741, 0.5385, 0.2026, 0.2424, 0.689, 0.3199, 0.6773, 0.7106, 0.5905, 0.5167, 0.3286, 0.6439, 0.5284, 0.6984, 0.2913, 0.2657, 0.8549, 0.2015, 0.4807, 0.812, 0.2975, 0.4294, 0.5854, 0.8226, 0.2159, 0.9024, 0.6231, 0.544, 0.2013, 0.056, 0.6253, 0.4995, 0.6434, 0.7946, 0.7389, 0.8958, 0.202, 0.522, 0.8025, 0.5325, 0.8145, 0.6209, 0.4823, 0.5402, 0.5517, 0.4125, 0.4192, 0.6163, 0.3467, 0.4021, 0.1143, 0.3608, 0.3225, 0.5075, 0.7793, 0.122, 0.6976, 0.6454, 0.5824, 0.4924, 0.3985, 0.662, 0.627, 0.4432, 0.6822, 0.4908, 0.2967, 0.8369, 0.1657, 0.6773, 0.2195, 0.2975, 0.4057, 0.639, 0.6657, 0.4319, 0.4003, 0.2334, 0.6208, 0.5181, 0.0566, 0.7515, 0.5527, 0.4288, 0.6363, 0.3293, 0.2904, 0.4036, 0.3029, 0.4134, 0.459, 0.3385, 0.4946, 0.3376, 0.7361, 0.3836, 0.5315, 0.7676, 0.3435, 0.5506, 0.744, 0.4892, 0.7333, 0.4093, 0.7627, 0.1817, 0.8957, 0.6717, 0.6922, 0.514, 0.4149, 0.4859, 0.6216, 0.2575, 0.5702, 0.2469, 0.4234, 0.6527, 0.7017, 0.2008, 0.2711, 0.394, 0.4435, 0.294, 0.671, 0.9173, 0.2359, 0.7393, 0.6188, 0.6145, 0.399, 0.1184, 0.2599, 0.4355, 0.3641, 0.2283, 0.5472, 0.338, 0.5048, 0.6987, 0.9105, 0.5089, 0.5823, 0.5823, 0.7797, 0.776, 0.5034, 0.2351, 0.5991, 0.5875, 0.4417, 0.4557, 0.6083, 0.1372, 0.4755, 0.4347, 0.8148, 0.4654, 0.7125, 0.1184, 0.5963, 0.6283, 0.3854, 0.3521, 0.1402, 0.7773, 0.2342, 0.4245, 0.3016, 0.5903, 0.5037, 0.5793, 0.2234, 0.5268, 0.8009, 0.7075, 0.3307, 0.364, 0.4287, 0.4314, 0.6905, 0.2618, 0.5045, 0.4892, 0.1094, 0.7231, 0.4814, 0.646, 0.7901, 0.2306, 0.6924, 0.2594, 0.3999, 0.6319, 0.4808, 0.0461, 0.4126, 0.1797, 0.6496, 0.3622, 0.6541, 0.4195, 0.6621, 0.6732, 0.4737, 0.3364, 0.3911, 0.631, 0.1178, 0.4661, 0.396, 0.2265, 0.3414, 0.127, 0.7729, 0.4262, 0.5126, 0.2712, 0.2555, 0.5412, 0.2519, 0.3077, 0.6587, 0.1269, 0.4331, 0.2574, 0.0599, 0.3895, 0.3499, 0.4775, 0.2944, 0.6998, 0.3509, 0.5388, 0.6473, 0.1749, 0.7146, 0.1999, 0.6332, 0.0507, 0.4689, 0.4038, 0.9271, 0.8369, 0.0883, 0.7074, 0.6466, 0.2954, 0.3043, 0.6502, 0.8088, 0.4695, 0.6125, 0.3501, 0.5907, 0.3044, 0.2022, 0.4788, 0.4067, 0.3121, 0.6116, 0.59, 0.4174, 0.1693, 0.5866, 0.3208, 0.5121, 0.3902, 0.5839, 0.7019, 0.4285, 0.6233, 0.6254, 0.1034, 0.0693, 0.466, 0.5175, 0.6383, 0.4802, 0.229, 0.4375, 0.3103, 0.154, 0.3966, 0.2315, 0.4124, 0.5415, 0.3397, 0.2307, 0.436, 0.771, 0.3145, 0.3735, 0.5762, 0.6358, 0.564, 0.6166, 0.3095, 0.501, 0.121, 0.9064, 0.7093, 0.7438, 0.6541, 0.1173, 0.5452, 0.8214, 0.4123, 0.6082, 0.7517, 0.4538, 0.2777, 0.7962, 0.6574, 0.4682, 0.2368, 0.4567, 0.2355, 0.5345, 0.4503, 0.5402, 0.7384, 0.6695, 0.8127, 0.6278, 0.3493, 0.3385, 0.7081, 0.5892, 0.5063, 0.3924, 0.5927, 0.2422, 0.4108, 0.6865, 0.8809, 0.0967, 0.4439, 0.4007, 0.3647, 0.1755, 0.7153, 0.5733, 0.6769, 0.1662, 0.6504, 0.1632, 0.237, 0.5867, 0.1846, 0.6588, 0.4118, 0.3249, 0.4153, 0.4453, 0.5448, 0.5883, 0.7193, 0.5316, 0.7418, 0.8798, 0.9355, 0.3498, 0.2328, 0.5936, 0.2338, 0.273, 0.2985, 0.8653, 0.3735, 0.2692, 0.211, 0.3964, 0.6181, 0.6361, 0.3473, 0.2067, 0.3389, 0.3958, 0.8231, 0.1027, 0.4068, 0.2074, 0.4882, 0.413, 0.5387, 0.4883, 0.2078, 0.0886, 0.4288, 0.3336, 0.4097, 0.2357, 0.9309, 0.5122, 0.4378, 0.3371, 0.5398, 0.6901, 0.5171, 0.1546, 0.4582, 0.4126, 0.4844, 0.2022, 0.3315, 0.4781, 0.2693, 0.3599, 0.5123, 0.4871, 0.6238, 0.3536, 0.6378, 0.3282, 0.9623, 0.336, 0.645, 0.3564, 0.1891, 0.3317, 0.2885, 0.401, 0.8151, 0.6573, 0.624, 0.4969, 0.312, 0.5581, 0.2596, 0.3817, 0.6774, 0.5296, 0.1105, 0.4181, 0.33, 0.5129, 0.7186, 0.6612, 0.5423, 0.4577, 0.265, 0.4399, 0.6796, 0.5189, 0.3573, 0.5866, 0.4577, 0.5802, 0.3087, 0.2727, 0.8247, 0.3712, 0.5201, 0.3133, 0.6795, 0.5844, 0.4302, 0.8264, 0.4248, 0.5542, 0.4234, 0.7045, 0.5, 0.3854, 0.3561, 0.314, 0.4019, 0.4201, 0.5705, 0.2433, 0.4863, 0.5623, 0.4916, 0.3453, 0.5946, 0.4964, 0.0401, 0.4614, 0.7506, 0.3171, 0.9838, 0.4726, 0.1292, 0.4274, 0.6393, 0.441, 0.5751, 0.4014, 0.3875, 0.3649, 0.4494, 0.2682, 0.6366, 0.6261, 0.5913, 0.5865, 0.2556, 0.2713, 0.4986, 0.6739, 0.3368, 0.6429, 0.2449, 0.7195, 0.5032, 0.292, 0.2064, 0.2166, 0.1791, 0.3882, 0.3425, 0.5404, 0.106, 0.3112, 0.0693, 0.0421, 0.4796, 0.315, 0.0407, 0.2818, 0.5272, 0.137, 0.6881, 0.3943, 0.4411, 0.0598, 0.5173, 0.9409, 0.8582, 0.8878, 0.0934, 0.302, 0.4049, 0.4319, 0.4204, 0.3951, 0.2247, 0.3921, 0.385, 0.2122, 0.8284, 0.1995, 0.6015, 0.6904, 0.0801, 0.8008, 0.4488, 0.4833, 0.3679, 0.225, 0.2797, 0.2721, 0.1633, 0.3579, 0.5126, 0.3579, 0.3441, 0.4557, 0.4933, 0.3556, 0.6668, 0.5466, 0.498, 0.1361, 0.4445]


pochti_theta=np.linspace(0,1,1000)
result=[]
result1=[]
for x in pochti_theta:
    result.append(func_pravda(x,vyborka))
    result1.append([x,func_pravda(x,vyborka)])
#print(result1)


result2=np.array(result1)
print(result2[result2[:,1].argmax()])
plt.plot(pochti_theta,result)
plt.vlines(vyborka,0,3,linestyles='dashed')
plt.title('?????????????? ?????????????????????????? ?????? ?????????????? ?????????????? 1000')
plt.show()