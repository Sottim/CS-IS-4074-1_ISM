# ISM Report: Evaluation of Vision Transformer Models for Gigapixel Histopathology Images (CS-IS-4074-1)

## Overview

This repository contains the Independent Student Module (ISM) report for CS-IS-4074-1, titled "Evaluation of vision transformer models for gigapixel histopathology images." The project focuses on leveraging advanced deep learning techniques, specifically Vision Transformer (ViT) architectures like Cell-ViT and CellViT-Plus, for the analysis of complex Whole Slide Images (WSIs) in digital pathology. The primary application area is Triple Negative Breast Cancer (TNBC), utilizing a comprehensive dataset from IISER, Pune.

## Key Objectives & Contributions

- **Dataset Characterization & Harmonization:** Detailed analysis of the IISER TNBC dataset, including WSI distribution across rounds, subtypes (ER, HER2, TNBC), and various histological/immunohistochemical stains (H&E, Ki-67, AR, etc.). Implemented data preprocessing pipelines, including conversion to pyramidal TIFF format.
- **Segmentation Technique Analysis:**
  - Exploration of traditional methods (Watershed algorithm) and (Snake algorithms) along with established deep learning models (Mask R-CNN).
  - In-depth application and evaluation of the Cell-ViT and CellViT-Plus models for cell instance segmentation and classification.
- **WSI Processing Pipeline:** Development of a systematic pipeline for:
  - Automated tissue masking.
  - Standardized patch extraction (1024x1024, 64-pixel overlap).
  - Stain normalization.
  - Inference to generate cell-level annotations (bounding boxes, centroids, cell types like Neoplastic, Epithelial, Inflammatory, Connective, Dead) and cell embeddings.
- **Comparative Analysis:**
  - Evaluation of Cell-ViT performance on H&E stained TNBC WSIs from the IISER dataset.
  - Extension to gallbladder WSIs from AIIMS, with a comparative look at Cellpose and Active Contour models.
  - Analysis of model performance across different Immunohistochemical (IHC) markers (CK5, E-cadherin, Claudin-3, Claudin-7, AR) on TNBC samples, highlighting model sensitivities and challenges.
- **Outcome & Deliverables:**
  - Generation of richly annotated histopathology datasets.
  - Insights into the practical application and limitations of ViT models in computational pathology, especially concerning stain variability and training data bias.
  - Preparation of data for secure transfer and collaborative research with IISER, Pune.

## Core Technologies & Datasets

- **Models:** Cell-ViT, CellViT-Plus, Watershed, Mask R-CNN, Cellpose, Active Contours.
- **Datasets:**
  - IISER TNBC Dataset (various rounds, H&E and IHC stains).
  - AIIMS Gallbladder WSI dataset.
- **Techniques:** Vision Transformers, Deep Learning, Image Segmentation, Cell Classification, Whole Slide Image Processing, Data Harmonization.
- **Tools:** Python, VIPS, OpenSlide, (assumed) PyTorch/TensorFlow.

## Report Structure

The full report (provided in LaTeX format) details:

1.  Introduction to Breast Cancer and TNBC.
2.  Detailed description and analysis of the IISER TNBC Dataset.
3.  Analysis of Segmentation Techniques (Watershed, Mask R-CNN, Cell-ViT).
    - Proposed Methodology for Cell-ViT application.
    - Data Harmonization and Technical Specifications.
    - Inference results and Cell Type Classification.
    - Annotation Data Structure.
4.  Analysis on Gallbladder WSI from AIIMS.
5.  Comparative Nuclei Segmentation on AIIMS Gallbladder WSI.
6.  Comparative Analysis of IHC Markers Across TNBC WSIs.
7.  Data Transfer Process.
8.  Conclusion.

## Author & Supervision

- **Submitted by:** Santosh Adhikari
- **Supervised by:** Professor Rintu Kutum
- **Departments:** Department of Computer Science, Koita Center For Digital Health Ashoka (KCDH-A)
