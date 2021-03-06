%******************************************************************************************************************%
% The Market-1501 dataset is collected with six cameras, open environment, in Tsinghua University.                 %
% A total of 1501 individuals are annotated. 751 individuals are used for training. There are 750 individuals for  % 
% testing, and in total 3368 query images.                                                                         %
% There are 19732 images in the test set, and 12936 images in the training set.                                    %
% If you use this dataset, please kindly cite our paper as,                                                        %
%                                                                                                                  %
% Liang Zheng*, Shengjin Wang, Liyue Shen*, Lu Tian*, Jiahao Bu, and Qi Tian. Person Re-identification Meets Image %
% Search. Technical Report, 2015.  (*equal contribution)                                                           %
%                                                                                                                  %
% This dataset should be used for research only. Please DO NOT distribute or use it for commercial purpose.        %
%******************************************************************************************************************%

%%%%%% Content in the Zip file%%%%%%%%%%
1. "bounding_box_test" file. This file contains 19732 images for testing. 
2. "bounding_box_train" file. This file contains 12936 images for training.
3. "query" file. It contains 3368 query images. Search is performed in the "bounding_box_test" file.
4. "gt_bbox" file. It contains 25259 images, all hand-drawn. The images correspond to all the 1501 individuals in the test and training set.It is used to distinguish "good" "junk" and "distractors".
5. "gt_query" file. For each of the 3368 queries, there are both good and junk relevant images (containing the same individual). This file contains the image index of the good and junk images. It is used during performance evaluation.


If you have any problem, please contact me at liangzheng06@gmail.com.

================
Naming Rule of the bboxes
In bbox "0001_c1s1_001051_00.jpg", "c1" is the first camera (there are totally 6 cameras).

"s1" is sequence 1 of camera 1. Here, a sequence was defined automatically by the camera. We suppose that the camera cannot store a whole video that is quite large, so it splits the video into equally large sequences. Two sequences, namely, "c1s1" and "c2s1" do not happen exactly at the same time. This is mainly because the starting time of the 6 cameras are not exactly the same (it takes time to turn on them). But, "c1s1" and "c2s1" are roughly at the same time period.

"001051" is the 1051th frame in the sequence "c1s1". The frame rate is 25 frames per sec.

As with the last two digits, remember we use the DPM detector. Then, for identity "0001", there may be multiple detected bounding boxes in the frame "c1s1_001051". In other words, a pedestrian in the image may have several bboxes by DPM. So, "00" means that this bounding box is the first one among the several.

==============
Names beginning with "0000" are distractors produced by DPM false detection.
Names beginning with "-1" are junks that are neither good nor bad DPM bboxes.

