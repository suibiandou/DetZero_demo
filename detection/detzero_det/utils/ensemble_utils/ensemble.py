import torch
import numpy as np

from .wbf_3d import weighted_boxes_fusion_3d, weighted_tracking_boxes_fusion_3d


def wbf_online(boxes, scores, labels):
    device = boxes.device
    dtype = boxes.dtype
    
    boxes_list = boxes.cpu().numpy()
    scores_list = scores.cpu().numpy()
    labels_list = labels.cpu().numpy()

    iou_thresh = [0.8, 0.6, 0.7]
    skip_box_thr = [0.1, 0.01, 0.01]
    boxes, scores, labels = weighted_boxes_fusion_3d(
        boxes_list=boxes_list,
        scores_list=scores_list,
        labels_list=labels_list,
        weights=None,
        iou_thr=iou_thresh,
        skip_box_thr=skip_box_thr,
        conf_type='avg',
        iou_type='3d',
        allows_overflow=False
    )
    boxes = torch.from_numpy(boxes).to(device)
    scores = torch.from_numpy(scores).to(device)
    labels = torch.from_numpy(labels).to(device)

    return boxes, scores, labels

def wbf_tracking_v1(boxes, scores, labels, obj_ids):
    device = boxes.device
    dtype = boxes.dtype
    
    boxes_list = boxes.cpu().numpy()
    scores_list = scores.cpu().numpy()
    labels_list = labels.cpu().numpy()
    obj_ids_list = obj_ids.cpu().numpy()

    iou_thresh = [0.8, 0.6, 0.7]
    skip_box_thr = [0.1, 0.01, 0.01]
    boxes, scores, labels, obj_ids = weighted_tracking_boxes_fusion_3d(
        boxes_list=boxes_list,
        scores_list=scores_list,
        labels_list=labels_list,
        obj_ids_list=obj_ids_list,
        weights=None,
        iou_thr=iou_thresh,
        skip_box_thr=skip_box_thr,
        conf_type='avg',
        iou_type='3d',
        allows_overflow=False
    )
    boxes = torch.from_numpy(boxes).to(device)
    scores = torch.from_numpy(scores).to(device)
    labels = torch.from_numpy(labels).to(device)
    obj_ids = torch.from_numpy(obj_ids).to(device)

    return boxes, scores, labels, obj_ids

def wbf_tracking_v2(boxes, scores, labels):
    device = boxes.device
    dtype = boxes.dtype
    
    boxes_list = boxes.cpu().numpy()
    scores_list = scores.cpu().numpy()
    labels_list = labels.cpu().numpy()

    iou_thresh = [0.8, 0.6, 0.7]
    skip_box_thr = [0.1, 0.01, 0.01]
    boxes, scores, labels = weighted_boxes_fusion_3d(
        boxes_list=boxes_list,
        scores_list=scores_list,
        labels_list=labels_list,
        weights=None,
        iou_thr=iou_thresh,
        skip_box_thr=skip_box_thr,
        conf_type='avg',
        iou_type='3d',
        allows_overflow=False
    )
    boxes = torch.from_numpy(boxes).to(device)
    scores = torch.from_numpy(scores).to(device)
    labels = torch.from_numpy(labels).to(device)

    return boxes, scores, labels

def wbf_offline(boxes, scores, labels):
    raise NotImplementedError
