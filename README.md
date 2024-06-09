
This repository automatically updates a list of the top 100 repositories related to ComfyUI based on the number of stars on GitHub.

### Automatically updated on: 2024-06-09
### Repositories by Tag:
- [Core](tags/Core.md) (1)
- [Custom Nodes](tags/CustomNodes.md) (62)
- [Integration](tags/Integration.md) (15)
- [Workflow Examples](tags/WorkflowExamples.md) (9)
- [Management](tags/Management.md) (8)
- [Video](tags/Video.md) (7)
- [3D](tags/3D.md) (4)
- [LLM](tags/LLM.md) (4)
- [Tutorials](tags/Tutorials.md) (2)
- [Resources](tags/Resources.md) (2)
- [Translation](tags/Translation.md) (2)
- [Acceleration](tags/Acceleration.md) (1)
- [Website](tags/Website.md) (1)
- [Chinese Language](tags/ChineseLanguage.md) (13)
- [Deprecated](tags/Deprecated.md) (2)

# TOP 1 - 5

<details><summary>Star History for TOP 1 - 5</summary><a href="https://api.star-history.com/svg?repos=comfyanonymous/ComfyUI,AbdullahAlfaraj/Auto-Photoshop-StableDiffusion-Plugin,ltdrdata/ComfyUI-Manager,ZHO-ZHO-ZHO/ComfyUI-Workflows-ZHO,LykosAI/StabilityMatrix&type=Date"><img src="https://api.star-history.com/svg?repos=comfyanonymous/ComfyUI,AbdullahAlfaraj/Auto-Photoshop-StableDiffusion-Plugin,ltdrdata/ComfyUI-Manager,ZHO-ZHO-ZHO/ComfyUI-Workflows-ZHO,LykosAI/StabilityMatrix&type=Date" alt="Star History Chart" width="500"></a></details>


## 1. comfyanonymous/ComfyUI


<a href='https://github.com/comfyanonymous/ComfyUI'>
<img src="https://avatars.githubusercontent.com/u/121283862?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/comfyanonymous/ComfyUI

**Stars**: `37.1k` | **Created at**: `2023-01-17` | **Last updated**: `2024-06-09` | **Tags**: `Core`


The most powerful and modular stable diffusion GUI, api and backend with a graph/nodes interface.
<details><summary>Included Nodes (179)</summary>

 - <sub>AddNoise</sub>, <sub>AlignYourStepsScheduler</sub>
 - <sub>BasicGuider</sub>, <sub>BasicScheduler</sub>
 - <sub>Canny</sub>, <sub>CFGGuider</sub>, <sub>CheckpointLoader</sub>, <sub>CheckpointLoaderSimple</sub>, <sub>CheckpointSave</sub>, <sub>CLIPAttentionMultiply</sub>, <sub>CLIPLoader</sub>, <sub>CLIPMergeAdd</sub>, <sub>CLIPMergeSimple</sub>, <sub>CLIPMergeSubtract</sub>, <sub>CLIPSave</sub>, <sub>CLIPSetLastLayer</sub>, <sub>CLIPTextEncode</sub>, <sub>CLIPTextEncodeControlnet</sub>, <sub>CLIPTextEncodeSDXL</sub>, <sub>CLIPTextEncodeSDXLRefiner</sub>, <sub>CLIPVisionEncode</sub>, <sub>CLIPVisionLoader</sub>, <sub>ConditioningAverage</sub>, <sub>ConditioningCombine</sub>, <sub>ConditioningConcat</sub>, <sub>ConditioningSetArea</sub>, <sub>ConditioningSetAreaPercentage</sub>, <sub>ConditioningSetAreaStrength</sub>, <sub>ConditioningSetMask</sub>, <sub>ConditioningSetTimestepRange</sub>, <sub>ConditioningZeroOut</sub>, <sub>ControlNetApply</sub>, <sub>ControlNetApplyAdvanced</sub>, <sub>ControlNetLoader</sub>, <sub>CropMask</sub>
 - <sub>DiffControlNetLoader</sub>, <sub>DifferentialDiffusion</sub>, <sub>DiffusersLoader</sub>, <sub>DisableNoise</sub>, <sub>DualCFGGuider</sub>, <sub>DualCLIPLoader</sub>
 - <sub>EmptyImage</sub>, <sub>EmptyLatentImage</sub>, <sub>ExponentialScheduler</sub>
 - <sub>FeatherMask</sub>, <sub>FlipSigmas</sub>, <sub>FreeU</sub>, <sub>FreeU_V2</sub>
 - <sub>GLIGENLoader</sub>, <sub>GLIGENTextBoxApply</sub>, <sub>GrowMask</sub>
 - <sub>HypernetworkLoader</sub>, <sub>HyperTile</sub>
 - <sub>ImageBatch</sub>, <sub>ImageBlend</sub>, <sub>ImageBlur</sub>, <sub>ImageColorToMask</sub>, <sub>ImageCompositeMasked</sub>, <sub>ImageCrop</sub>, <sub>ImageFromBatch</sub>, <sub>ImageInvert</sub>, <sub>ImageOnlyCheckpointLoader</sub>, <sub>ImageOnlyCheckpointSave</sub>, <sub>ImagePadForOutpaint</sub>, <sub>ImageQuantize</sub>, <sub>ImageScale</sub>, <sub>ImageScaleBy</sub>, <sub>ImageScaleToTotalPixels</sub>, <sub>ImageSharpen</sub>, <sub>ImageToMask</sub>, <sub>ImageUpscaleWithModel</sub>, <sub>InpaintModelConditioning</sub>, <sub>InstructPixToPixConditioning</sub>, <sub>InvertMask</sub>
 - <sub>JoinImageWithAlpha</sub>
 - <sub>KarrasScheduler</sub>, <sub>KSampler</sub>, <sub>KSamplerAdvanced</sub>, <sub>KSamplerSelect</sub>
 - <sub>LatentAdd</sub>, <sub>LatentBatch</sub>, <sub>LatentBatchSeedBehavior</sub>, <sub>LatentBlend</sub>, <sub>LatentComposite</sub>, <sub>LatentCompositeMasked</sub>, <sub>LatentCrop</sub>, <sub>LatentFlip</sub>, <sub>LatentFromBatch</sub>, <sub>LatentInterpolate</sub>, <sub>LatentMultiply</sub>, <sub>LatentRotate</sub>, <sub>LatentSubtract</sub>, <sub>LatentUpscale</sub>, <sub>LatentUpscaleBy</sub>, <sub>LoadImage</sub>, <sub>LoadImageMask</sub>, <sub>LoadLatent</sub>, <sub>LoraLoader</sub>, <sub>LoraLoaderModelOnly</sub>
 - <sub>MaskComposite</sub>, <sub>MaskToImage</sub>, <sub>ModelMergeAdd</sub>, <sub>ModelMergeBlocks</sub>, <sub>ModelMergeSD1</sub>, <sub>ModelMergeSD2</sub>, <sub>ModelMergeSDXL</sub>, <sub>ModelMergeSimple</sub>, <sub>ModelMergeSubtract</sub>, <sub>ModelSamplingContinuousEDM</sub>, <sub>ModelSamplingDiscrete</sub>, <sub>ModelSamplingStableCascade</sub>, <sub>Morphology</sub>
 - <sub>PatchModelAddDownscale</sub>, <sub>PerpNeg</sub>, <sub>PerpNegGuider</sub>, <sub>PerturbedAttentionGuidance</sub>, <sub>PhotoMakerEncode</sub>, <sub>PhotoMakerLoader</sub>, <sub>PolyexponentialScheduler</sub>, <sub>PorterDuffImageComposite</sub>, <sub>PreviewImage</sub>
 - <sub>RandomNoise</sub>, <sub>RebatchImages</sub>, <sub>RebatchLatents</sub>, <sub>RepeatImageBatch</sub>, <sub>RepeatLatentBatch</sub>, <sub>RescaleCFG</sub>
 - <sub>SamplerCustom</sub>, <sub>SamplerCustomAdvanced</sub>, <sub>SamplerDPMAdaptative</sub>, <sub>SamplerDPMPP_2M_SDE</sub>, <sub>SamplerDPMPP_3M_SDE</sub>, <sub>SamplerDPMPP_SDE</sub>, <sub>SamplerEulerAncestral</sub>, <sub>SamplerLCMUpscale</sub>, <sub>SamplerLMS</sub>, <sub>SaveAnimatedPNG</sub>, <sub>SaveAnimatedWEBP</sub>, <sub>SaveImage</sub>, <sub>SaveImageWebsocket</sub>, <sub>SaveLatent</sub>, <sub>SD_4XUpscale_Conditioning</sub>, <sub>SDTurboScheduler</sub>, <sub>SelfAttentionGuidance</sub>, <sub>SetLatentNoiseMask</sub>, <sub>SolidMask</sub>, <sub>SplitImageWithAlpha</sub>, <sub>SplitSigmas</sub>, <sub>SplitSigmasDenoise</sub>, <sub>StableCascade_EmptyLatentImage</sub>, <sub>StableCascade_StageB_Conditioning</sub>, <sub>StableCascade_StageC_VAEEncode</sub>, <sub>StableCascade_SuperResolutionControlnet</sub>, <sub>StableZero123_Conditioning</sub>, <sub>StableZero123_Conditioning_Batched</sub>, <sub>StyleModelApply</sub>, <sub>StyleModelLoader</sub>, <sub>SV3D_Conditioning</sub>, <sub>SVD_img2vid_Conditioning</sub>
 - <sub>ThresholdMask</sub>, <sub>TomePatchModel</sub>
 - <sub>unCLIPCheckpointLoader</sub>, <sub>unCLIPConditioning</sub>, <sub>UNetCrossAttentionMultiply</sub>, <sub>UNETLoader</sub>, <sub>UNetSelfAttentionMultiply</sub>, <sub>UNetTemporalAttentionMultiply</sub>, <sub>UpscaleModelLoader</sub>
 - <sub>VAEDecode</sub>, <sub>VAEDecodeTiled</sub>, <sub>VAEEncode</sub>, <sub>VAEEncodeForInpaint</sub>, <sub>VAEEncodeTiled</sub>, <sub>VAELoader</sub>, <sub>VAESave</sub>, <sub>VideoLinearCFGGuidance</sub>, <sub>VideoTriangleCFGGuidance</sub>, <sub>VPScheduler</sub>
 - <sub>WebcamCapture</sub>
</details>


## 2. AbdullahAlfaraj/Auto-Photoshop-StableDiffusion-Plugin


<a href='https://github.com/AbdullahAlfaraj/Auto-Photoshop-StableDiffusion-Plugin'>
<img src="https://avatars.githubusercontent.com/u/7842232?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/AbdullahAlfaraj/Auto-Photoshop-StableDiffusion-Plugin

**Stars**: `6.4k` | **Created at**: `2022-12-20` | **Last updated**: `2024-06-09` | **Tags**: `Integration`


A user-friendly plug-in that makes it easy to generate stable diffusion images inside Photoshop using either Automatic or ComfyUI as a backend.

## 3. ltdrdata/ComfyUI-Manager


<a href='https://github.com/ltdrdata/ComfyUI-Manager'>
<img src="https://avatars.githubusercontent.com/u/128333288?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/ltdrdata/ComfyUI-Manager

**Stars**: `4.1k` | **Created at**: `2023-04-23` | **Last updated**: `2024-06-09` | **Tags**: `Management`


ComfyUI-Manager is an extension designed to enhance the usability of ComfyUI. It offers management functions to install, remove, disable, and enable various custom nodes of ComfyUI. Furthermore, this extension provides a hub feature and convenience functions to access a wide range of information within ComfyUI.

## 4. ZHO-ZHO-ZHO/ComfyUI-Workflows-ZHO


<a href='https://github.com/ZHO-ZHO-ZHO/ComfyUI-Workflows-ZHO'>
<img src="https://avatars.githubusercontent.com/u/140084057?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/ZHO-ZHO-ZHO/ComfyUI-Workflows-ZHO

**Stars**: `3.6k` | **Created at**: `2024-03-06` | **Last updated**: `2024-06-08` | **Tags**: `Workflow Examples` `Chinese Language`


我的 ComfyUI 工作流合集 | My ComfyUI workflows collection

## 5. LykosAI/StabilityMatrix


<a href='https://github.com/LykosAI/StabilityMatrix'>
<img src="https://avatars.githubusercontent.com/u/136279213?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/LykosAI/StabilityMatrix

**Stars**: `3.1k` | **Created at**: `2023-06-13` | **Last updated**: `2024-06-09` | **Tags**: `Integration`


Multi-Platform Package Manager for Stable Diffusion
# TOP 6 - 10

<details><summary>Star History for TOP 6 - 10</summary><a href="https://api.star-history.com/svg?repos=cubiq/ComfyUI_IPAdapter_plus,Kosinkadink/ComfyUI-AnimateDiff-Evolved,mut-ex/gligen-gui,FurkanGozukara/Stable-Diffusion,6174/comflowyspace&type=Date"><img src="https://api.star-history.com/svg?repos=cubiq/ComfyUI_IPAdapter_plus,Kosinkadink/ComfyUI-AnimateDiff-Evolved,mut-ex/gligen-gui,FurkanGozukara/Stable-Diffusion,6174/comflowyspace&type=Date" alt="Star History Chart" width="500"></a></details>


## 6. cubiq/ComfyUI_IPAdapter_plus


<a href='https://github.com/cubiq/ComfyUI_IPAdapter_plus'>
<img src="https://avatars.githubusercontent.com/u/427614?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/cubiq/ComfyUI_IPAdapter_plus

**Stars**: `2.9k` | **Created at**: `2023-08-30` | **Last updated**: `2024-06-09` | **Tags**: `Custom Nodes`


None
<details><summary>Included Nodes (30)</summary>

 - <sub>IPAAdapterFaceIDBatch</sub>, <sub>IPAdapter</sub>, <sub>IPAdapterAdvanced</sub>, <sub>IPAdapterBatch</sub>, <sub>IPAdapterCombineEmbeds</sub>, <sub>IPAdapterCombineParams</sub>, <sub>IPAdapterCombineWeights</sub>, <sub>IPAdapterEmbeds</sub>, <sub>IPAdapterEmbedsBatch</sub>, <sub>IPAdapterEncoder</sub>, <sub>IPAdapterFaceID</sub>, <sub>IPAdapterFromParams</sub>, <sub>IPAdapterInsightFaceLoader</sub>, <sub>IPAdapterLoadEmbeds</sub>, <sub>IPAdapterModelLoader</sub>, <sub>IPAdapterMS</sub>, <sub>IPAdapterNoise</sub>, <sub>IPAdapterPromptScheduleFromWeightsStrategy</sub>, <sub>IPAdapterRegionalConditioning</sub>, <sub>IPAdapterSaveEmbeds</sub>, <sub>IPAdapterStyleComposition</sub>, <sub>IPAdapterStyleCompositionBatch</sub>, <sub>IPAdapterTiled</sub>, <sub>IPAdapterTiledBatch</sub>, <sub>IPAdapterUnifiedLoader</sub>, <sub>IPAdapterUnifiedLoaderCommunity</sub>, <sub>IPAdapterUnifiedLoaderFaceID</sub>, <sub>IPAdapterWeights</sub>, <sub>IPAdapterWeightsFromStrategy</sub>
 - <sub>PrepImageForClipVision</sub>
</details>


## 7. Kosinkadink/ComfyUI-AnimateDiff-Evolved


<a href='https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved'>
<img src="https://avatars.githubusercontent.com/u/7365912?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/Kosinkadink/ComfyUI-AnimateDiff-Evolved

**Stars**: `2.2k` | **Created at**: `2023-08-26` | **Last updated**: `2024-06-09` | **Tags**: `Custom Nodes`


Improved AnimateDiff for ComfyUI and Advanced Sampling Support
<details><summary>Included Nodes (87)</summary>

 - <sub>ADE_AdjustPEFullStretch</sub>, <sub>ADE_AdjustPEManual</sub>, <sub>ADE_AdjustPESweetspotStretch</sub>, <sub>ADE_AdjustWeightAllAdd</sub>, <sub>ADE_AdjustWeightAllMult</sub>, <sub>ADE_AdjustWeightIndivAdd</sub>, <sub>ADE_AdjustWeightIndivAttnAdd</sub>, <sub>ADE_AdjustWeightIndivAttnMult</sub>, <sub>ADE_AdjustWeightIndivMult</sub>, <sub>[ADE_AnimateDiffCombine](node_examples/ADE_AnimateDiffCombine.md)</sub>, <sub>[ADE_AnimateDiffKeyframe](node_examples/ADE_AnimateDiffKeyframe.md)</sub>, <sub>[ADE_AnimateDiffLoaderGen1](node_examples/ADE_AnimateDiffLoaderGen1.md)</sub>, <sub>[ADE_AnimateDiffLoaderV1Advanced](node_examples/ADE_AnimateDiffLoaderV1Advanced.md)</sub>, [ADE_AnimateDiffLoaderWithContext🌟](node_examples/ADE_AnimateDiffLoaderWithContext.md), [ADE_AnimateDiffLoRALoader🌟](node_examples/ADE_AnimateDiffLoRALoader.md), <sub>ADE_AnimateDiffModelSettings</sub>, <sub>ADE_AnimateDiffModelSettings_Release</sub>, <sub>[ADE_AnimateDiffModelSettingsAdvancedAttnStrengths](node_examples/ADE_AnimateDiffModelSettingsAdvancedAttnStrengths.md)</sub>, <sub>[ADE_AnimateDiffModelSettingsSimple](node_examples/ADE_AnimateDiffModelSettingsSimple.md)</sub>, [ADE_AnimateDiffSamplingSettings🌟](node_examples/ADE_AnimateDiffSamplingSettings.md), <sub>ADE_AnimateDiffSettings</sub>, [ADE_AnimateDiffUniformContextOptions🌟](node_examples/ADE_AnimateDiffUniformContextOptions.md), <sub>[ADE_AnimateDiffUnload](node_examples/ADE_AnimateDiffUnload.md)</sub>, [ADE_ApplyAnimateDiffModel🌟](node_examples/ADE_ApplyAnimateDiffModel.md), <sub>[ADE_ApplyAnimateDiffModelSimple](node_examples/ADE_ApplyAnimateDiffModelSimple.md)</sub>, <sub>ADE_ApplyAnimateDiffModelWithCameraCtrl</sub>, <sub>ADE_ApplyAnimateLCMI2VModel</sub>, <sub>ADE_AttachLoraHookToCLIP</sub>, <sub>ADE_AttachLoraHookToConditioning</sub>, <sub>[ADE_BatchedContextOptions](node_examples/ADE_BatchedContextOptions.md)</sub>, <sub>ADE_CameraCtrlAnimateDiffKeyframe</sub>, <sub>ADE_CameraManualPoseAppend</sub>, <sub>ADE_CameraPoseAdvanced</sub>, <sub>ADE_CameraPoseBasic</sub>, <sub>ADE_CameraPoseCombo</sub>, <sub>ADE_CombineLoraHooks</sub>, <sub>ADE_CombineLoraHooksEight</sub>, <sub>ADE_CombineLoraHooksFour</sub>, <sub>ADE_ConditioningSetMask</sub>, <sub>ADE_ConditioningSetMaskAndCombine</sub>, <sub>ADE_ConditioningSetUnmaskedAndCombine</sub>, <sub>ADE_CustomCFG</sub>, <sub>ADE_CustomCFGKeyframe</sub>, <sub>ADE_EmptyLatentImageLarge</sub>, <sub>ADE_InjectI2VIntoAnimateDiffModel</sub>, <sub>ADE_IterationOptsDefault</sub>, <sub>ADE_IterationOptsFreeInit</sub>, <sub>ADE_LoadAnimateDiffModel</sub>, <sub>ADE_LoadAnimateDiffModelWithCameraCtrl</sub>, <sub>ADE_LoadAnimateLCMI2VModel</sub>, <sub>ADE_LoadCameraPoses</sub>, <sub>ADE_LoopedUniformContextOptions</sub>, <sub>ADE_LoopedUniformViewOptions</sub>, <sub>ADE_LoraHookKeyframe</sub>, <sub>ADE_LoraHookKeyframeFromStrengthList</sub>, <sub>ADE_LoraHookKeyframeInterpolation</sub>, <sub>ADE_MaskedLoadLora</sub>, <sub>ADE_MultivalDynamic</sub>, <sub>ADE_MultivalScaledMask</sub>, <sub>ADE_NoiseLayerAdd</sub>, <sub>ADE_NoiseLayerAddWeighted</sub>, <sub>ADE_NoiseLayerReplace</sub>, <sub>ADE_PairedConditioningSetMask</sub>, <sub>ADE_PairedConditioningSetMaskAndCombine</sub>, <sub>ADE_PairedConditioningSetUnmaskedAndCombine</sub>, <sub>ADE_RawSigmaSchedule</sub>, <sub>ADE_RegisterLoraHook</sub>, <sub>ADE_RegisterLoraHookModelOnly</sub>, <sub>ADE_RegisterModelAsLoraHook</sub>, <sub>ADE_RegisterModelAsLoraHookModelOnly</sub>, <sub>ADE_ReplaceCameraParameters</sub>, <sub>ADE_ReplaceOriginalPoseAspectRatio</sub>, <sub>ADE_SetLoraHookKeyframe</sub>, <sub>ADE_SigmaSchedule</sub>, <sub>ADE_SigmaScheduleSplitAndCombine</sub>, <sub>ADE_SigmaScheduleWeightedAverage</sub>, <sub>ADE_SigmaScheduleWeightedAverageInterp</sub>, <sub>ADE_StandardStaticContextOptions</sub>, <sub>ADE_StandardStaticViewOptions</sub>, <sub>ADE_StandardUniformContextOptions</sub>, <sub>ADE_StandardUniformViewOptions</sub>, <sub>ADE_TimestepsConditioning</sub>, <sub>ADE_UpscaleAndVAEEncode</sub>, <sub>ADE_UseEvolvedSampling</sub>, <sub>ADE_ViewsOnlyContextOptions</sub>, <sub>AnimateDiffLoaderV1</sub>
 - <sub>CheckpointLoaderSimpleWithNoiseSelect</sub>
</details>


## 8. mut-ex/gligen-gui


<a href='https://github.com/mut-ex/gligen-gui'>
<img src="https://avatars.githubusercontent.com/u/21265981?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/mut-ex/gligen-gui

**Stars**: `1.9k` | **Created at**: `2024-02-17` | **Last updated**: `2024-06-09` | **Tags**: `Integration`


An intuitive GUI for GLIGEN that uses ComfyUI in the backend

## 9. FurkanGozukara/Stable-Diffusion


<a href='https://github.com/FurkanGozukara/Stable-Diffusion'>
<img src="https://avatars.githubusercontent.com/u/19240467?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/FurkanGozukara/Stable-Diffusion

**Stars**: `1.8k` | **Created at**: `2023-05-01` | **Last updated**: `2024-06-09` | **Tags**: `Tutorials`


Stable Diffusion, SDXL, LoRA Training, DreamBooth Training, Automatic1111 Web UI, DeepFake, Deep Fakes, TTS, Animation, Text To Video, Tutorials, Guides, Lectures, Courses, ComfyUI, Google Colab, RunPod, NoteBooks, ControlNet, TTS, Voice Cloning, AI, AI News, ML, ML News, News, Tech, Tech News, Kohya LoRA, Kandinsky 2, DeepFloyd IF, Midjourney

## 10. 6174/comflowyspace


<a href='https://github.com/6174/comflowyspace'>
<img src="https://avatars.githubusercontent.com/u/3872872?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/6174/comflowyspace

**Stars**: `1.7k` | **Created at**: `2023-11-25` | **Last updated**: `2024-06-08` | **Tags**: `Integration`


Comflowyspace is an intuitive, user-friendly, open-source AI tool for generating images and videos, democratizing access to AI technology.
# TOP 11 - 15

<details><summary>Star History for TOP 11 - 15</summary><a href="https://api.star-history.com/svg?repos=MrForExample/ComfyUI-3D-Pack,Fannovel16/comfyui_controlnet_aux,ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn,siliconflow/onediff,ltdrdata/ComfyUI-Impact-Pack&type=Date"><img src="https://api.star-history.com/svg?repos=MrForExample/ComfyUI-3D-Pack,Fannovel16/comfyui_controlnet_aux,ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn,siliconflow/onediff,ltdrdata/ComfyUI-Impact-Pack&type=Date" alt="Star History Chart" width="500"></a></details>


## 11. MrForExample/ComfyUI-3D-Pack


<a href='https://github.com/MrForExample/ComfyUI-3D-Pack'>
<img src="https://avatars.githubusercontent.com/u/62230687?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/MrForExample/ComfyUI-3D-Pack

**Stars**: `1.6k` | **Created at**: `2024-01-05` | **Last updated**: `2024-06-09` | **Tags**: `Custom Nodes` `3D`


An extensive node suite that enables ComfyUI to process 3D inputs (Mesh & UV Texture, etc) using cutting edge algorithms (3DGS, NeRF, etc.)
<details><summary>Included Nodes (0)?</summary>

 - Sorry, we can't get the node list for this project since it lacks conventional `NODE_CLASS_MAPPINGS` and doesn't have a `node_list.json` file to specify the node details according to [ComfyUI-Manager's support guide](https://github.com/ltdrdata/ComfyUI-Manager#custom-node-support-guide)</details>


## 12. Fannovel16/comfyui_controlnet_aux


<a href='https://github.com/Fannovel16/comfyui_controlnet_aux'>
<img src="https://avatars.githubusercontent.com/u/16047777?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/Fannovel16/comfyui_controlnet_aux

**Stars**: `1.5k` | **Created at**: `2023-08-17` | **Last updated**: `2024-06-09` | **Tags**: `Custom Nodes`


ComfyUI's ControlNet Auxiliary Preprocessors
<details><summary>Included Nodes (58)</summary>

 - <sub>AIO_Preprocessor</sub>, <sub>AnimalPosePreprocessor</sub>, <sub>AnimeFace_SemSegPreprocessor</sub>, <sub>AnimeLineArtPreprocessor</sub>, <sub>AnyLineArtPreprocessor_aux</sub>
 - <sub>BAE-NormalMapPreprocessor</sub>, <sub>BinaryPreprocessor</sub>
 - <sub>CannyEdgePreprocessor</sub>, <sub>ColorPreprocessor</sub>, <sub>ControlNetPreprocessorSelector</sub>
 - <sub>DensePosePreprocessor</sub>, <sub>DepthAnythingPreprocessor</sub>, <sub>DiffusionEdge_Preprocessor</sub>, <sub>DSINE-NormalMapPreprocessor</sub>, <sub>DWPreprocessor</sub>
 - <sub>FacialPartColoringFromPoseKps</sub>, <sub>FakeScribblePreprocessor</sub>
 - <sub>HEDPreprocessor</sub>, <sub>HintImageEnchance</sub>
 - <sub>ImageGenResolutionFromImage</sub>, <sub>ImageGenResolutionFromLatent</sub>, <sub>ImageIntensityDetector</sub>, <sub>ImageLuminanceDetector</sub>, <sub>InpaintPreprocessor</sub>
 - <sub>LeReS-DepthMapPreprocessor</sub>, <sub>LineArtPreprocessor</sub>, <sub>LineartStandardPreprocessor</sub>
 - <sub>M-LSDPreprocessor</sub>, <sub>Manga2Anime_LineArt_Preprocessor</sub>, <sub>MaskOptFlow</sub>, <sub>MediaPipe-FaceMeshPreprocessor</sub>, <sub>MeshGraphormer+ImpactDetector-DepthMapPreprocessor</sub>, <sub>MeshGraphormer-DepthMapPreprocessor</sub>, <sub>Metric3D-DepthMapPreprocessor</sub>, <sub>Metric3D-NormalMapPreprocessor</sub>, <sub>MiDaS-DepthMapPreprocessor</sub>, <sub>MiDaS-NormalMapPreprocessor</sub>
 - <sub>OneFormer-ADE20K-SemSegPreprocessor</sub>, <sub>OneFormer-COCO-SemSegPreprocessor</sub>, <sub>OpenposePreprocessor</sub>
 - <sub>PiDiNetPreprocessor</sub>, <sub>PixelPerfectResolution</sub>
 - <sub>SAMPreprocessor</sub>, <sub>SavePoseKpsAsJsonFile</sub>, <sub>Scribble_PiDiNet_Preprocessor</sub>, <sub>Scribble_XDoG_Preprocessor</sub>, <sub>ScribblePreprocessor</sub>, <sub>SemSegPreprocessor</sub>, <sub>ShufflePreprocessor</sub>
 - <sub>TEEDPreprocessor</sub>, <sub>TilePreprocessor</sub>, <sub>TTPlanet_TileGF_Preprocessor</sub>, <sub>TTPlanet_TileSimple_Preprocessor</sub>
 - <sub>UniFormer-SemSegPreprocessor</sub>, <sub>Unimatch_OptFlowPreprocessor</sub>, <sub>UpperBodyTrackingFromPoseKps</sub>
 - <sub>Zoe-DepthMapPreprocessor</sub>, <sub>Zoe_DepthAnythingPreprocessor</sub>
</details>


## 13. ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn


<a href='https://github.com/ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn'>
<img src="https://avatars.githubusercontent.com/u/140084057?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn

**Stars**: `1.4k` | **Created at**: `2023-12-15` | **Last updated**: `2024-06-09` | **Tags**: `Custom Nodes` `Chinese Language`


肖像大师 中文版 comfyui-portrait-master
<details><summary>Included Nodes (1)</summary>

 - <sub>PortraitMaster_中文版</sub>
</details>


## 14. siliconflow/onediff


<a href='https://github.com/siliconflow/onediff'>
<img src="https://avatars.githubusercontent.com/u/143005960?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/siliconflow/onediff

**Stars**: `1.3k` | **Created at**: `2022-09-21` | **Last updated**: `2024-06-09` | **Tags**: `Acceleration`


OneDiff: An out-of-the-box acceleration library for diffusion models.

## 15. ltdrdata/ComfyUI-Impact-Pack


<a href='https://github.com/ltdrdata/ComfyUI-Impact-Pack'>
<img src="https://avatars.githubusercontent.com/u/128333288?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/ltdrdata/ComfyUI-Impact-Pack

**Stars**: `1.3k` | **Created at**: `2023-03-30` | **Last updated**: `2024-06-08` | **Tags**: `Custom Nodes`


Custom nodes pack for ComfyUI This custom node helps to conveniently enhance images through Detector, Detailer, Upscaler, Pipe, and more.
<details><summary>Included Nodes (187)</summary>

 - <sub>AddMask</sub>
 - <sub>BasicPipeToDetailerPipe</sub>, <sub>BasicPipeToDetailerPipeSDXL</sub>, <sub>BboxDetectorCombined</sub>, <sub>BboxDetectorCombined_v2</sub>, <sub>BboxDetectorForEach</sub>, <sub>BboxDetectorSEGS</sub>, <sub>BitwiseAndMask</sub>, <sub>BitwiseAndMaskForEach</sub>
 - <sub>CfgScheduleHookProvider</sub>, <sub>CLIPSegDetectorProvider</sub>, <sub>CombineRegionalPrompts</sub>, <sub>CoreMLDetailerHookProvider</sub>, <sub>CustomNoiseDetailerHookProvider</sub>
 - <sub>DenoiseScheduleHookProvider</sub>, <sub>DenoiseSchedulerDetailerHookProvider</sub>, <sub>DetailerForEach</sub>, <sub>DetailerForEachDebug</sub>, <sub>DetailerForEachDebugPipe</sub>, <sub>DetailerForEachPipe</sub>, <sub>DetailerForEachPipeForAnimateDiff</sub>, <sub>DetailerHookCombine</sub>, <sub>DetailerPipeToBasicPipe</sub>
 - <sub>EditBasicPipe</sub>, <sub>EditDetailerPipe</sub>, <sub>EditDetailerPipeSDXL</sub>, <sub>EmptySegs</sub>
 - <sub>FaceDetailer</sub>, <sub>FaceDetailerPipe</sub>, <sub>FromBasicPipe</sub>, <sub>FromBasicPipe_v2</sub>, <sub>FromDetailerPipe</sub>, <sub>FromDetailerPipe_v2</sub>, <sub>FromDetailerPipeSDXL</sub>
 - <sub>ImageListToImageBatch</sub>, <sub>ImageMaskSwitch</sub>, <sub>ImageReceiver</sub>, <sub>ImageSender</sub>, <sub>ImpactAssembleSEGS</sub>, <sub>ImpactCombineConditionings</sub>, <sub>ImpactCompare</sub>, <sub>ImpactConcatConditionings</sub>, <sub>ImpactConditionalBranch</sub>, <sub>ImpactConditionalBranchSelMode</sub>, <sub>ImpactConditionalStopIteration</sub>, <sub>ImpactControlBridge</sub>, <sub>ImpactControlNetApplyAdvancedSEGS</sub>, <sub>ImpactControlNetApplySEGS</sub>, <sub>ImpactControlNetClearSEGS</sub>, <sub>ImpactConvertDataType</sub>, <sub>ImpactDecomposeSEGS</sub>, <sub>ImpactDilate_Mask_SEG_ELT</sub>, <sub>ImpactDilateMask</sub>, <sub>ImpactDilateMaskInSEGS</sub>, <sub>ImpactDummyInput</sub>, <sub>ImpactEdit_SEG_ELT</sub>, <sub>ImpactFloat</sub>, <sub>ImpactFrom_SEG_ELT</sub>, <sub>ImpactFrom_SEG_ELT_bbox</sub>, <sub>ImpactFrom_SEG_ELT_crop_region</sub>, <sub>ImpactGaussianBlurMask</sub>, <sub>ImpactGaussianBlurMaskInSEGS</sub>, <sub>ImpactHFTransformersClassifierProvider</sub>, <sub>ImpactIfNone</sub>, <sub>ImpactImageBatchToImageList</sub>, <sub>ImpactImageInfo</sub>, <sub>ImpactInt</sub>, <sub>ImpactInversedSwitch</sub>, <sub>ImpactIPAdapterApplySEGS</sub>, <sub>ImpactIsNotEmptySEGS</sub>, <sub>ImpactKSamplerAdvancedBasicPipe</sub>, <sub>ImpactKSamplerBasicPipe</sub>, <sub>ImpactLatentInfo</sub>, <sub>ImpactLogger</sub>, <sub>ImpactLogicalOperators</sub>, <sub>ImpactMakeImageBatch</sub>, <sub>ImpactMakeImageList</sub>, <sub>ImpactMakeTileSEGS</sub>, <sub>ImpactMinMax</sub>, <sub>ImpactNeg</sub>, <sub>ImpactNodeSetMuteState</sub>, <sub>ImpactQueueTrigger</sub>, <sub>ImpactQueueTriggerCountdown</sub>, <sub>ImpactRemoteBoolean</sub>, <sub>ImpactRemoteInt</sub>, <sub>ImpactScaleBy_BBOX_SEG_ELT</sub>, <sub>ImpactSchedulerAdapter</sub>, <sub>ImpactSegsAndMask</sub>, <sub>ImpactSegsAndMaskForEach</sub>, <sub>ImpactSEGSClassify</sub>, <sub>ImpactSEGSConcat</sub>, <sub>ImpactSEGSLabelAssign</sub>, <sub>ImpactSEGSLabelFilter</sub>, <sub>ImpactSEGSOrderedFilter</sub>, <sub>ImpactSEGSPicker</sub>, <sub>ImpactSEGSRangeFilter</sub>, <sub>ImpactSEGSToMaskBatch</sub>, <sub>ImpactSEGSToMaskList</sub>, <sub>ImpactSetWidgetValue</sub>, <sub>ImpactSimpleDetectorSEGS</sub>, <sub>ImpactSimpleDetectorSEGS_for_AD</sub>, <sub>ImpactSimpleDetectorSEGSPipe</sub>, <sub>ImpactSleep</sub>, <sub>ImpactStringSelector</sub>, <sub>ImpactSwitch</sub>, <sub>ImpactValueReceiver</sub>, <sub>ImpactValueSender</sub>, <sub>ImpactWildcardEncode</sub>, <sub>ImpactWildcardProcessor</sub>, <sub>IterativeImageUpscale</sub>, <sub>IterativeLatentUpscale</sub>
 - <sub>KSamplerAdvancedProvider</sub>, <sub>KSamplerProvider</sub>
 - <sub>LatentPixelScale</sub>, <sub>LatentReceiver</sub>, <sub>LatentSender</sub>, <sub>LatentSwitch</sub>
 - <sub>MaskDetailerPipe</sub>, <sub>MaskListToMaskBatch</sub>, <sub>MaskPainter</sub>, <sub>MasksToMaskList</sub>, <sub>MaskToSEGS</sub>, <sub>MaskToSEGS_for_AnimateDiff</sub>, <sub>MediaPipeFaceMeshToSEGS</sub>, <sub>MMDetDetectorProvider</sub>, <sub>MMDetLoader</sub>
 - <sub>NoiseInjectionDetailerHookProvider</sub>, <sub>NoiseInjectionHookProvider</sub>
 - <sub>ONNXDetectorProvider</sub>, <sub>ONNXDetectorSEGS</sub>
 - <sub>PixelKSampleHookCombine</sub>, <sub>PixelKSampleUpscalerProvider</sub>, <sub>PixelKSampleUpscalerProviderPipe</sub>, <sub>PixelTiledKSampleUpscalerProvider</sub>, <sub>PixelTiledKSampleUpscalerProviderPipe</sub>, <sub>PreviewBridge</sub>, <sub>PreviewBridgeLatent</sub>, <sub>PreviewDetailerHookProvider</sub>
 - <sub>ReencodeLatent</sub>, <sub>ReencodeLatentPipe</sub>, <sub>RegionalPrompt</sub>, <sub>RegionalSampler</sub>, <sub>RegionalSamplerAdvanced</sub>, <sub>RemoveImageFromSEGS</sub>, <sub>RemoveNoiseMask</sub>
 - <sub>SAMDetectorCombined</sub>, <sub>SAMDetectorSegmented</sub>, <sub>SAMLoader</sub>, <sub>SegmDetectorCombined</sub>, <sub>SegmDetectorCombined_v2</sub>, <sub>SegmDetectorForEach</sub>, <sub>SegmDetectorSEGS</sub>, <sub>Segs  Mask</sub>, <sub>Segs  Mask ForEach</sub>, <sub>SEGSDetailer</sub>, <sub>SEGSDetailerForAnimateDiff</sub>, <sub>SEGSLabelFilterDetailerHookProvider</sub>, <sub>SegsMaskCombine</sub>, <sub>SEGSOrderedFilterDetailerHookProvider</sub>, <sub>SEGSPaste</sub>, <sub>SEGSPreview</sub>, <sub>SEGSPreviewCNet</sub>, <sub>SEGSRangeFilterDetailerHookProvider</sub>, <sub>SEGSSwitch</sub>, <sub>SegsToCombinedMask</sub>, <sub>SEGSToImageList</sub>, <sub>SEGSUpscaler</sub>, <sub>SEGSUpscalerPipe</sub>, <sub>SetDefaultImageForSEGS</sub>, <sub>StepsScheduleHookProvider</sub>, <sub>StringListToString</sub>, <sub>SubtractMask</sub>, <sub>SubtractMaskForEach</sub>
 - <sub>TiledKSamplerProvider</sub>, <sub>ToBasicPipe</sub>, <sub>ToBinaryMask</sub>, <sub>ToDetailerPipe</sub>, <sub>ToDetailerPipeSDXL</sub>, <sub>TwoAdvancedSamplersForMask</sub>, <sub>TwoSamplersForMask</sub>, <sub>TwoSamplersForMaskUpscalerProvider</sub>, <sub>TwoSamplersForMaskUpscalerProviderPipe</sub>
 - <sub>UltralyticsDetectorProvider</sub>, <sub>UnsamplerDetailerHookProvider</sub>, <sub>UnsamplerHookProvider</sub>
 - <sub>VariationNoiseDetailerHookProvider</sub>
 - <sub>WildcardPromptFromString</sub>
</details>

# TOP 16 - 20

<details><summary>Star History for TOP 16 - 20</summary><a href="https://api.star-history.com/svg?repos=pythongosssss/ComfyUI-Custom-Scripts,huchenlei/ComfyUI-layerdiffuse,fofr/cog-face-to-many,ZHO-ZHO-ZHO/ComfyUI-InstantID,comfyanonymous/ComfyUI_examples&type=Date"><img src="https://api.star-history.com/svg?repos=pythongosssss/ComfyUI-Custom-Scripts,huchenlei/ComfyUI-layerdiffuse,fofr/cog-face-to-many,ZHO-ZHO-ZHO/ComfyUI-InstantID,comfyanonymous/ComfyUI_examples&type=Date" alt="Star History Chart" width="500"></a></details>


## 16. pythongosssss/ComfyUI-Custom-Scripts


<a href='https://github.com/pythongosssss/ComfyUI-Custom-Scripts'>
<img src="https://avatars.githubusercontent.com/u/125205205?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/pythongosssss/ComfyUI-Custom-Scripts

**Stars**: `1.3k` | **Created at**: `2023-03-06` | **Last updated**: `2024-06-09` | **Tags**: `Custom Nodes` `Management`


Enhancements & experiments for ComfyUI, mostly focusing on UI features
<details><summary>Included Nodes (14)</summary>

 - <sub>CheckpointLoader|pysssss</sub>, <sub>ConstrainImageforVideo|pysssss</sub>, <sub>ConstrainImage|pysssss</sub>
 - <sub>LoadText|pysssss</sub>, <sub>LoraLoader|pysssss</sub>
 - <sub>MathExpression|pysssss</sub>, <sub>MultiPrimitive|pysssss</sub>
 - <sub>PlaySound|pysssss</sub>
 - <sub>Repeater|pysssss</sub>, <sub>ReroutePrimitive|pysssss</sub>
 - <sub>SaveText|pysssss</sub>, <sub>ShowText|pysssss</sub>, <sub>StringFunction|pysssss</sub>, <sub>SystemNotification|pysssss</sub>
</details>


## 17. huchenlei/ComfyUI-layerdiffuse


<a href='https://github.com/huchenlei/ComfyUI-layerdiffuse'>
<img src="https://avatars.githubusercontent.com/u/20929282?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/huchenlei/ComfyUI-layerdiffuse

**Stars**: `1.2k` | **Created at**: `2024-03-02` | **Last updated**: `2024-06-08` | **Tags**: `Custom Nodes`


Layer Diffuse custom nodes
<details><summary>Included Nodes (8)</summary>

 - <sub>LayeredDiffusionApply</sub>, <sub>LayeredDiffusionCondApply</sub>, <sub>LayeredDiffusionCondJointApply</sub>, <sub>LayeredDiffusionDecode</sub>, <sub>LayeredDiffusionDecodeRGBA</sub>, <sub>LayeredDiffusionDecodeSplit</sub>, <sub>LayeredDiffusionDiffApply</sub>, <sub>LayeredDiffusionJointApply</sub>
</details>


## 18. fofr/cog-face-to-many


<a href='https://github.com/fofr/cog-face-to-many'>
<img src="https://avatars.githubusercontent.com/u/319055?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/fofr/cog-face-to-many

**Stars**: `1.2k` | **Created at**: `2024-03-05` | **Last updated**: `2024-06-08` | **Tags**: `Workflow Examples`


Turn any face into a video game character, pixel art, claymation, 3D or toy

## 19. ZHO-ZHO-ZHO/ComfyUI-InstantID


<a href='https://github.com/ZHO-ZHO-ZHO/ComfyUI-InstantID'>
<img src="https://avatars.githubusercontent.com/u/140084057?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/ZHO-ZHO-ZHO/ComfyUI-InstantID

**Stars**: `1.2k` | **Created at**: `2024-01-22` | **Last updated**: `2024-06-09` | **Tags**: `Custom Nodes` `Chinese Language`


Unofficial implementation of InstantID for ComfyUI
<details><summary>Included Nodes (7)</summary>

 - <sub>ID_Prompt_Styler</sub>, <sub>IDBaseModelLoader_fromhub</sub>, <sub>IDBaseModelLoader_local</sub>, <sub>IDControlNetLoader</sub>, <sub>IDGenerationNode</sub>, <sub>InsightFaceLoader_Zho</sub>, <sub>Ipadapter_instantidLoader</sub>
</details>


## 20. comfyanonymous/ComfyUI_examples


<a href='https://github.com/comfyanonymous/ComfyUI_examples'>
<img src="https://avatars.githubusercontent.com/u/121283862?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/comfyanonymous/ComfyUI_examples

**Stars**: `1.2k` | **Created at**: `2023-01-30` | **Last updated**: `2024-06-09` | **Tags**: `Workflow Examples`


Examples of ComfyUI workflows
# TOP 21 - 25

<details><summary>Star History for TOP 21 - 25</summary><a href="https://api.star-history.com/svg?repos=kijai/ComfyUI-SUPIR,nerdyrodent/AVeryComfyNerd,mcmonkeyprojects/sd-dynamic-thresholding,Gourieff/comfyui-reactor-node,WASasquatch/was-node-suite-comfyui&type=Date"><img src="https://api.star-history.com/svg?repos=kijai/ComfyUI-SUPIR,nerdyrodent/AVeryComfyNerd,mcmonkeyprojects/sd-dynamic-thresholding,Gourieff/comfyui-reactor-node,WASasquatch/was-node-suite-comfyui&type=Date" alt="Star History Chart" width="500"></a></details>


## 21. kijai/ComfyUI-SUPIR


<a href='https://github.com/kijai/ComfyUI-SUPIR'>
<img src="https://avatars.githubusercontent.com/u/40791699?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/kijai/ComfyUI-SUPIR

**Stars**: `1.1k` | **Created at**: `2024-02-28` | **Last updated**: `2024-06-09` | **Tags**: `Custom Nodes`


SUPIR upscaling wrapper for ComfyUI
<details><summary>Included Nodes (10)</summary>

 - <sub>SUPIR_conditioner</sub>, <sub>SUPIR_decode</sub>, <sub>SUPIR_encode</sub>, <sub>SUPIR_first_stage</sub>, <sub>SUPIR_model_loader</sub>, <sub>SUPIR_model_loader_v2</sub>, <sub>SUPIR_model_loader_v2_clip</sub>, <sub>SUPIR_sample</sub>, <sub>SUPIR_tiles</sub>, <sub>SUPIR_Upscale</sub>
</details>


## 22. nerdyrodent/AVeryComfyNerd


<a href='https://github.com/nerdyrodent/AVeryComfyNerd'>
<img src="https://avatars.githubusercontent.com/u/74688049?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/nerdyrodent/AVeryComfyNerd

**Stars**: `1.1k` | **Created at**: `2023-08-17` | **Last updated**: `2024-06-09` | **Tags**: `Resources`


ComfyUI related stuff and things

## 23. mcmonkeyprojects/sd-dynamic-thresholding


<a href='https://github.com/mcmonkeyprojects/sd-dynamic-thresholding'>
<img src="https://avatars.githubusercontent.com/u/43497670?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/mcmonkeyprojects/sd-dynamic-thresholding

**Stars**: `1.0k` | **Created at**: `2023-01-27` | **Last updated**: `2024-06-07` | **Tags**: `Custom Nodes`


Dynamic Thresholding (CFG Scale Fix) for Stable Diffusion (StableSwarmUI, ComfyUI, and Auto WebUI)
<details><summary>Included Nodes (2)</summary>

 - <sub>DynamicThresholdingFull</sub>, <sub>DynamicThresholdingSimple</sub>
</details>


## 24. Gourieff/comfyui-reactor-node


<a href='https://github.com/Gourieff/comfyui-reactor-node'>
<img src="https://avatars.githubusercontent.com/u/85128026?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/Gourieff/comfyui-reactor-node

**Stars**: `1.0k` | **Created at**: `2023-08-02` | **Last updated**: `2024-06-09` | **Tags**: `Custom Nodes`


Fast and Simple Face Swap Extension Node for ComfyUI
<details><summary>Included Nodes (11)</summary>

 - <sub>ImageRGBA2RGB</sub>
 - <sub>ReActorBuildFaceModel</sub>, <sub>ReActorFaceSwap</sub>, <sub>ReActorFaceSwapOpt</sub>, <sub>ReActorImageDublicator</sub>, <sub>ReActorLoadFaceModel</sub>, <sub>ReActorMakeFaceModelBatch</sub>, <sub>ReActorMaskHelper</sub>, <sub>ReActorOptions</sub>, <sub>ReActorRestoreFace</sub>, <sub>ReActorSaveFaceModel</sub>
</details>


## 25. WASasquatch/was-node-suite-comfyui


<a href='https://github.com/WASasquatch/was-node-suite-comfyui'>
<img src="https://avatars.githubusercontent.com/u/1151589?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/WASasquatch/was-node-suite-comfyui

**Stars**: `900` | **Created at**: `2023-03-24` | **Last updated**: `2024-06-08` | **Tags**: `Custom Nodes`


An extensive node suite for ComfyUI with over 210 new nodes
<details><summary>Included Nodes (214)</summary>

 - <sub>Blend Latents</sub>, <sub>BLIP Analyze Image</sub>, <sub>BLIP Model Loader</sub>, <sub>Boolean To Text</sub>, <sub>Bounded Image Blend</sub>, <sub>Bounded Image Blend with Mask</sub>, <sub>Bounded Image Crop</sub>, <sub>Bounded Image Crop with Mask</sub>, <sub>Bus Node</sub>
 - <sub>Cache Node</sub>, <sub>Checkpoint Loader</sub>, <sub>Checkpoint Loader (Simple)</sub>, <sub>CLIP Input Switch</sub>, <sub>CLIP Vision Input Switch</sub>, <sub>CLIPSeg Batch Masking</sub>, <sub>CLIPSeg Masking</sub>, <sub>CLIPSeg Model Loader</sub>, <sub>CLIPTextEncode (BlenderNeko Advanced + NSP)</sub>, <sub>CLIPTextEncode (NSP)</sub>, <sub>Conditioning Input Switch</sub>, <sub>Constant Number</sub>, <sub>Control Net Model Input Switch</sub>, <sub>Convert Masks to Images</sub>, <sub>Create Grid Image</sub>, <sub>Create Grid Image from Batch</sub>, <sub>Create Morph Image</sub>, <sub>Create Morph Image from Path</sub>, <sub>Create Video from Path</sub>
 - <sub>Debug Number to Console</sub>, <sub>Dictionary to Console</sub>, <sub>Diffusers Hub Model Down-Loader</sub>, <sub>Diffusers Model Loader</sub>
 - <sub>Export API</sub>
 - <sub>Image Analyze</sub>, <sub>Image Aspect Ratio</sub>, <sub>Image Batch</sub>, <sub>Image Blank</sub>, <sub>Image Blend</sub>, <sub>Image Blend by Mask</sub>, <sub>Image Blending Mode</sub>, <sub>Image Bloom Filter</sub>, <sub>Image Bounds</sub>, <sub>Image Bounds to Console</sub>, <sub>Image Canny Filter</sub>, <sub>Image Chromatic Aberration</sub>, <sub>Image Color Palette</sub>, <sub>Image Crop Face</sub>, <sub>Image Crop Location</sub>, <sub>Image Crop Square Location</sub>, <sub>Image Displacement Warp</sub>, <sub>Image Dragan Photography Filter</sub>, <sub>Image Edge Detection Filter</sub>, <sub>Image fDOF Filter</sub>, <sub>Image Film Grain</sub>, <sub>Image Filter Adjustments</sub>, <sub>Image Flip</sub>, <sub>Image Generate Gradient</sub>, <sub>Image Gradient Map</sub>, <sub>Image High Pass Filter</sub>, <sub>Image History Loader</sub>, <sub>Image Input Switch</sub>, <sub>Image Levels Adjustment</sub>, <sub>Image Load</sub>, <sub>Image Lucy Sharpen</sub>, <sub>Image Median Filter</sub>, <sub>Image Mix RGB Channels</sub>, <sub>Image Monitor Effects Filter</sub>, <sub>Image Nova Filter</sub>, <sub>Image Padding</sub>, <sub>Image Paste Crop</sub>, <sub>Image Paste Crop by Location</sub>, <sub>Image Paste Face</sub>, <sub>Image Perlin Noise</sub>, <sub>Image Perlin Power Fractal</sub>, <sub>Image Pixelate</sub>, <sub>Image Power Noise</sub>, <sub>Image Rembg (Remove Background)</sub>, <sub>Image Remove Background (Alpha)</sub>, <sub>Image Remove Color</sub>, <sub>Image Resize</sub>, <sub>Image Rotate</sub>, <sub>Image Rotate Hue</sub>, <sub>Image Save</sub>, <sub>Image Seamless Texture</sub>, <sub>Image Select Channel</sub>, <sub>Image Select Color</sub>, <sub>Image Shadows and Highlights</sub>, <sub>Image Size to Number</sub>, <sub>Image SSAO (Ambient Occlusion)</sub>, <sub>Image SSDO (Direct Occlusion)</sub>, <sub>Image Stitch</sub>, <sub>Image Style Filter</sub>, <sub>Image Threshold</sub>, <sub>Image Tiled</sub>, <sub>Image to Latent Mask</sub>, <sub>Image to Noise</sub>, <sub>Image to Seed</sub>, <sub>Image Transpose</sub>, <sub>Image Voronoi Noise Filter</sub>, <sub>Images to Linear</sub>, <sub>Images to RGB</sub>, <sub>Inset Image Bounds</sub>, <sub>Integer place counter</sub>
 - <sub>KSampler (WAS)</sub>, <sub>KSampler Cycle</sub>
 - <sub>Latent Batch</sub>, <sub>Latent Input Switch</sub>, <sub>Latent Noise Injection</sub>, <sub>Latent Size to Number</sub>, <sub>Latent Upscale by Factor (WAS)</sub>, <sub>Load Cache</sub>, <sub>Load Image Batch</sub>, <sub>Load Lora</sub>, <sub>Load Text File</sub>, <sub>Logic Boolean</sub>, <sub>Logic Boolean Primitive</sub>, <sub>Logic Comparison AND</sub>, <sub>Logic Comparison OR</sub>, <sub>Logic Comparison XOR</sub>, <sub>Logic NOT</sub>, <sub>Lora Input Switch</sub>, <sub>Lora Loader</sub>
 - <sub>Mask Arbitrary Region</sub>, <sub>Mask Batch</sub>, <sub>Mask Batch to Mask</sub>, <sub>Mask Ceiling Region</sub>, <sub>Mask Crop Dominant Region</sub>, <sub>Mask Crop Minority Region</sub>, <sub>Mask Crop Region</sub>, <sub>Mask Dilate Region</sub>, <sub>Mask Dominant Region</sub>, <sub>Mask Erode Region</sub>, <sub>Mask Fill Holes</sub>, <sub>Mask Floor Region</sub>, <sub>Mask Gaussian Region</sub>, <sub>Mask Invert</sub>, <sub>Mask Minority Region</sub>, <sub>Mask Paste Region</sub>, <sub>Mask Smooth Region</sub>, <sub>Mask Threshold Region</sub>, <sub>Masks Add</sub>, <sub>Masks Combine Batch</sub>, <sub>Masks Combine Regions</sub>, <sub>Masks Subtract</sub>, <sub>MiDaS Depth Approximation</sub>, <sub>MiDaS Mask Image</sub>, <sub>MiDaS Model Loader</sub>, <sub>Model Input Switch</sub>
 - <sub>Number Counter</sub>, <sub>Number Input Condition</sub>, <sub>Number Input Switch</sub>, <sub>Number Multiple Of</sub>, <sub>Number Operation</sub>, <sub>Number PI</sub>, <sub>Number to Float</sub>, <sub>Number to Int</sub>, <sub>Number to Seed</sub>, <sub>Number to String</sub>, <sub>Number to Text</sub>
 - <sub>Prompt Multiple Styles Selector</sub>, <sub>Prompt Styles Selector</sub>
 - <sub>Random Number</sub>
 - <sub>SAM Image Mask</sub>, <sub>SAM Model Loader</sub>, <sub>SAM Parameters</sub>, <sub>SAM Parameters Combine</sub>, <sub>Samples Passthrough (Stat System)</sub>, <sub>Save Text File</sub>, <sub>Seed</sub>, <sub>String to Text</sub>
 - <sub>Tensor Batch to Image</sub>, <sub>Text Add Token by Input</sub>, <sub>Text Add Tokens</sub>, <sub>Text Compare</sub>, <sub>Text Concatenate</sub>, <sub>Text Contains</sub>, <sub>Text Dictionary Convert</sub>, <sub>Text Dictionary Get</sub>, <sub>Text Dictionary Keys</sub>, <sub>Text Dictionary New</sub>, <sub>Text Dictionary To Text</sub>, <sub>Text Dictionary Update</sub>, <sub>Text File History Loader</sub>, <sub>Text Find</sub>, <sub>Text Find and Replace</sub>, <sub>Text Find and Replace by Dictionary</sub>, <sub>Text Find and Replace Input</sub>, <sub>Text Input Switch</sub>, <sub>Text List</sub>, <sub>Text List Concatenate</sub>, <sub>Text List to Text</sub>, <sub>Text Load Line From File</sub>, <sub>Text Multiline</sub>, <sub>Text Multiline (Code Compatible)</sub>, <sub>Text Parse A1111 Embeddings</sub>, <sub>Text Parse Noodle Soup Prompts</sub>, <sub>Text Parse Tokens</sub>, <sub>Text Random Line</sub>, <sub>Text Random Prompt</sub>, <sub>Text Shuffle</sub>, <sub>Text String</sub>, <sub>Text String Truncate</sub>, <sub>Text to Conditioning</sub>, <sub>Text to Console</sub>, <sub>Text to Number</sub>, <sub>Text to String</sub>, <sub>True Random.org Number Generator</sub>
 - <sub>unCLIP Checkpoint Loader</sub>, <sub>Upscale Model Loader</sub>, <sub>Upscale Model Switch</sub>
 - <sub>VAE Input Switch</sub>, <sub>Video Dump Frames</sub>
 - <sub>Write to GIF</sub>, <sub>Write to Video</sub>
</details>

# TOP 26 - 30

<details><summary>Star History for TOP 26 - 30</summary><a href="https://api.star-history.com/svg?repos=zanllp/sd-webui-infinite-image-browsing,cubiq/ComfyUI_InstantID,shadowcz007/comfyui-mixlab-nodes,AIGODLIKE/AIGODLIKE-ComfyUI-Translation,6174/comflowy&type=Date"><img src="https://api.star-history.com/svg?repos=zanllp/sd-webui-infinite-image-browsing,cubiq/ComfyUI_InstantID,shadowcz007/comfyui-mixlab-nodes,AIGODLIKE/AIGODLIKE-ComfyUI-Translation,6174/comflowy&type=Date" alt="Star History Chart" width="500"></a></details>


## 26. zanllp/sd-webui-infinite-image-browsing


<a href='https://github.com/zanllp/sd-webui-infinite-image-browsing'>
<img src="https://avatars.githubusercontent.com/u/25872019?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/zanllp/sd-webui-infinite-image-browsing

**Stars**: `881` | **Created at**: `2023-03-07` | **Last updated**: `2024-06-09` | **Tags**: `Management`


A fast and powerful image/video browser for Stable Diffusion webui / ComfyUI / Fooocus / NovelAI, featuring infinite scrolling and advanced search capabilities using image parameters. It also supports standalone operation.

## 27. cubiq/ComfyUI_InstantID


<a href='https://github.com/cubiq/ComfyUI_InstantID'>
<img src="https://avatars.githubusercontent.com/u/427614?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/cubiq/ComfyUI_InstantID

**Stars**: `863` | **Created at**: `2024-01-27` | **Last updated**: `2024-06-07` | **Tags**: `Custom Nodes`


None
<details><summary>Included Nodes (7)</summary>

 - <sub>ApplyInstantID</sub>, <sub>ApplyInstantIDAdvanced</sub>, <sub>ApplyInstantIDControlNet</sub>
 - <sub>FaceKeypointsPreprocessor</sub>
 - <sub>InstantIDAttentionPatch</sub>, <sub>InstantIDFaceAnalysis</sub>, <sub>InstantIDModelLoader</sub>
</details>


## 28. shadowcz007/comfyui-mixlab-nodes


<a href='https://github.com/shadowcz007/comfyui-mixlab-nodes'>
<img src="https://avatars.githubusercontent.com/u/12645064?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/shadowcz007/comfyui-mixlab-nodes

**Stars**: `843` | **Created at**: `2023-10-18` | **Last updated**: `2024-06-09` | **Tags**: `Custom Nodes` `Chinese Language`


Workflow-to-APP、ScreenShare&FloatingVideo、GPT & 3D、SpeechRecognition&TTS
<details><summary>Included Nodes (86)</summary>

 - <sub>[3DImage](node_examples/3DImage.md)</sub>
 - <sub>AppInfo</sub>, <sub>ApplyVisualStylePrompting_</sub>, <sub>AreaToMask</sub>
 - <sub>CenterImage</sub>, <sub>CharacterInText</sub>, <sub>ChatGPTOpenAI</sub>, <sub>CkptNames_</sub>, <sub>Color</sub>, <sub>ComparingTwoFrames_</sub>, <sub>CompositeImages_</sub>
 - <sub>DynamicDelayProcessor</sub>
 - <sub>EmbeddingPrompt</sub>, <sub>EnhanceImage</sub>
 - <sub>FaceToMask</sub>, <sub>FeatheredMask</sub>, <sub>FloatingVideo</sub>, <sub>FloatSlider</sub>, <sub>Font</sub>
 - <sub>GamePal</sub>, <sub>GetImageSize_</sub>, <sub>GLIGENTextBoxApply_Advanced</sub>, <sub>GradientImage</sub>, <sub>GridDisplayAndSave</sub>, <sub>GridInput</sub>, <sub>GridOutput</sub>
 - <sub>ImageColorTransfer</sub>, <sub>ImageCropByAlpha</sub>, <sub>ImageListReplace_</sub>, <sub>ImagesPrompt_</sub>, <sub>IncrementingListNode_</sub>, <sub>IntNumber</sub>
 - <sub>JoinWithDelimiter</sub>
 - <sub>LimitNumber</sub>, <sub>ListSplit_</sub>, <sub>LoadImagesFromPath</sub>, <sub>LoadImagesFromURL</sub>, <sub>LoadImagesToBatch</sub>, <sub>LoadTripoSRModel_</sub>, <sub>LoadVideoAndSegment_</sub>, <sub>LoraNames_</sub>, <sub>LoraPrompt</sub>
 - <sub>MaskListMerge_</sub>, <sub>MaskListReplace_</sub>, <sub>MergeLayers</sub>, <sub>MirroredImage</sub>, <sub>MultiplicationNode</sub>
 - <sub>NewLayer</sub>, <sub>NoiseImage</sub>
 - <sub>OutlineMask</sub>
 - <sub>PreviewMask_</sub>, <sub>PromptImage</sub>, <sub>PromptSimplification</sub>, <sub>PromptSlide</sub>
 - <sub>RandomPrompt</sub>, <sub>ResizeImageMixlab</sub>
 - <sub>SamplerNames_</sub>, <sub>SaveImageAndMetadata_</sub>, <sub>SaveImageToLocal</sub>, <sub>SaveTripoSRMesh</sub>, <sub>ScreenShare</sub>, <sub>Seed_</sub>, <sub>ShowLayer</sub>, <sub>ShowTextForGPT</sub>, <sub>SmoothMask</sub>, <sub>SpeechRecognition</sub>, <sub>SpeechSynthesis</sub>, <sub>SplitImage</sub>, <sub>SplitLongMask</sub>, <sub>StyleAlignedBatchAlign_</sub>, <sub>StyleAlignedReferenceSampler_</sub>, <sub>StyleAlignedSampleReferenceLatents_</sub>, <sub>SvgImage</sub>, <sub>SwitchByIndex</sub>
 - <sub>TESTNODE_</sub>, <sub>TESTNODE_TOKEN</sub>, <sub>TextImage</sub>, <sub>TextInput_</sub>, <sub>TextSplitByDelimiter</sub>, <sub>TextToNumber</sub>, <sub>TransparentImage</sub>, <sub>TripoSRSampler_</sub>
 - <sub>VAEDecodeConsistencyDecoder</sub>, <sub>VAEEncodeForInpaint_Frames</sub>, <sub>VAELoaderConsistencyDecoder</sub>, <sub>VideoCombine_Adv</sub>
</details>


## 29. AIGODLIKE/AIGODLIKE-ComfyUI-Translation


<a href='https://github.com/AIGODLIKE/AIGODLIKE-ComfyUI-Translation'>
<img src="https://avatars.githubusercontent.com/u/124877023?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/AIGODLIKE/AIGODLIKE-ComfyUI-Translation

**Stars**: `820` | **Created at**: `2023-08-15` | **Last updated**: `2024-06-09` | **Tags**: `Translation`


A plugin for multilingual translation of ComfyUI，This plugin implements translation of resident menu bar/search bar/right-click context menu/node, etc

## 30. 6174/comflowy


<a href='https://github.com/6174/comflowy'>
<img src="https://avatars.githubusercontent.com/u/3872872?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/6174/comflowy

**Stars**: `807` | **Created at**: `2023-11-20` | **Last updated**: `2024-06-07` | **Tags**: `Website`


Unleash endless possibilities with ComfyUI and Stable Diffusion, committed to crafting refined AI-Gen tools and cultivating a vibrant community for both developers and users. 
# TOP 31 - 35

<details><summary>Star History for TOP 31 - 35</summary><a href="https://api.star-history.com/svg?repos=pydn/ComfyUI-to-Python-Extension,11cafe/comfyui-workspace-manager,ZHO-ZHO-ZHO/ComfyUI-PhotoMaker-ZHO,florestefano1975/comfyui-portrait-master,SeargeDP/SeargeSDXL&type=Date"><img src="https://api.star-history.com/svg?repos=pydn/ComfyUI-to-Python-Extension,11cafe/comfyui-workspace-manager,ZHO-ZHO-ZHO/ComfyUI-PhotoMaker-ZHO,florestefano1975/comfyui-portrait-master,SeargeDP/SeargeSDXL&type=Date" alt="Star History Chart" width="500"></a></details>


## 31. pydn/ComfyUI-to-Python-Extension


<a href='https://github.com/pydn/ComfyUI-to-Python-Extension'>
<img src="https://avatars.githubusercontent.com/u/25550995?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/pydn/ComfyUI-to-Python-Extension

**Stars**: `790` | **Created at**: `2023-07-30` | **Last updated**: `2024-06-08` | **Tags**: `Integration`


A powerful tool that translates ComfyUI workflows into executable Python code.

## 32. 11cafe/comfyui-workspace-manager


<a href='https://github.com/11cafe/comfyui-workspace-manager'>
<img src="https://avatars.githubusercontent.com/u/152708197?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/11cafe/comfyui-workspace-manager

**Stars**: `757` | **Created at**: `2023-12-02` | **Last updated**: `2024-06-07` | **Tags**: `Management`


A ComfyUI workflows and models management extension to organize and manage all your workflows, models in one place. Seamlessly switch between workflows, as well as import, export workflows, reuse subworkflows, install models, browse your models in a single workspace

## 33. ZHO-ZHO-ZHO/ComfyUI-PhotoMaker-ZHO


<a href='https://github.com/ZHO-ZHO-ZHO/ComfyUI-PhotoMaker-ZHO'>
<img src="https://avatars.githubusercontent.com/u/140084057?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/ZHO-ZHO-ZHO/ComfyUI-PhotoMaker-ZHO

**Stars**: `740` | **Created at**: `2024-01-15` | **Last updated**: `2024-06-08` | **Tags**: `Custom Nodes` `Chinese Language`


Unofficial implementation of PhotoMaker for ComfyUI
<details><summary>Included Nodes (9)</summary>

 - <sub>BaseModel_Loader_fromhub</sub>, <sub>BaseModel_Loader_local</sub>
 - <sub>LoRALoader</sub>
 - <sub>NEW_PhotoMaker_Generation</sub>
 - <sub>PhotoMaker_Generation</sub>, <sub>PhotoMakerAdapter_Loader_fromhub</sub>, <sub>PhotoMakerAdapter_Loader_local</sub>, <sub>Prompt_Styler</sub>
 - <sub>Ref_Image_Preprocessing</sub>
</details>


## 34. florestefano1975/comfyui-portrait-master


<a href='https://github.com/florestefano1975/comfyui-portrait-master'>
<img src="https://avatars.githubusercontent.com/u/153757302?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/florestefano1975/comfyui-portrait-master

**Stars**: `732` | **Created at**: `2023-12-13` | **Last updated**: `2024-06-09` | **Tags**: `Custom Nodes`


This node was designed to help AI image creators to generate prompts for human portraits.
<details><summary>Included Nodes (1)</summary>

 - <sub>PortraitMaster</sub>
</details>


## 35. SeargeDP/SeargeSDXL


<a href='https://github.com/SeargeDP/SeargeSDXL'>
<img src="https://avatars.githubusercontent.com/u/3330978?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/SeargeDP/SeargeSDXL

**Stars**: `731` | **Created at**: `2023-07-12` | **Last updated**: `2024-06-08` | **Tags**: `Custom Nodes` `Workflow Examples`


Custom nodes and workflows for SDXL in ComfyUI
<details><summary>Included Nodes (73)</summary>

 - <sub>SeargeAdvancedParameters</sub>, <sub>SeargeCheckpointLoader</sub>, <sub>SeargeConditioningMuxer2</sub>, <sub>SeargeConditioningMuxer5</sub>, <sub>SeargeConditioningParameters</sub>, <sub>SeargeConditionMixing</sub>, <sub>SeargeControlnetAdapterV2</sub>, <sub>SeargeControlnetModels</sub>, <sub>SeargeCustomAfterUpscaling</sub>, <sub>SeargeCustomAfterVaeDecode</sub>, <sub>SeargeCustomPromptMode</sub>, <sub>SeargeDebugPrinter</sub>, <sub>SeargeEnablerInputs</sub>, <sub>SeargeFloatConstant</sub>, <sub>SeargeFloatMath</sub>, <sub>SeargeFloatPair</sub>, <sub>SeargeFreeU</sub>, <sub>SeargeGenerated1</sub>, <sub>SeargeGenerationParameters</sub>, <sub>SeargeHighResolution</sub>, <sub>SeargeImage2ImageAndInpainting</sub>, <sub>SeargeImageAdapterV2</sub>, <sub>SeargeImageSave</sub>, <sub>SeargeImageSaving</sub>, <sub>SeargeInput1</sub>, <sub>SeargeInput2</sub>, <sub>SeargeInput3</sub>, <sub>SeargeInput4</sub>, <sub>SeargeInput5</sub>, <sub>SeargeInput6</sub>, <sub>SeargeInput7</sub>, <sub>SeargeIntegerConstant</sub>, <sub>SeargeIntegerMath</sub>, <sub>SeargeIntegerPair</sub>, <sub>SeargeIntegerScaler</sub>, <sub>SeargeLatentMuxer3</sub>, <sub>SeargeLoraLoader</sub>, <sub>SeargeLoras</sub>, <sub>SeargeMagicBox</sub>, <sub>SeargeModelSelector</sub>, <sub>SeargeOperatingMode</sub>, <sub>SeargeOutput1</sub>, <sub>SeargeOutput2</sub>, <sub>SeargeOutput3</sub>, <sub>SeargeOutput4</sub>, <sub>SeargeOutput5</sub>, <sub>SeargeOutput6</sub>, <sub>SeargeOutput7</sub>, <sub>SeargeParameterProcessor</sub>, <sub>SeargePipelineStart</sub>, <sub>SeargePipelineTerminator</sub>, <sub>SeargePreviewImage</sub>, <sub>SeargePromptAdapterV2</sub>, <sub>SeargePromptCombiner</sub>, <sub>SeargePromptStyles</sub>, <sub>SeargePromptText</sub>, <sub>SeargeSamplerAdvanced</sub>, <sub>SeargeSamplerInputs</sub>, <sub>SeargeSaveFolderInputs</sub>, <sub>SeargeSDXLBasePromptEncoder</sub>, <sub>SeargeSDXLImage2ImageSampler</sub>, <sub>SeargeSDXLImage2ImageSampler2</sub>, <sub>SeargeSDXLPromptEncoder</sub>, <sub>SeargeSDXLRefinerPromptEncoder</sub>, <sub>SeargeSDXLSampler</sub>, <sub>SeargeSDXLSampler2</sub>, <sub>SeargeSDXLSamplerV3</sub>, <sub>SeargeSeparator</sub>, <sub>SeargeStylePreprocessor</sub>, <sub>SeargeTextInputV2</sub>, <sub>SeargeUpscaleModelLoader</sub>, <sub>SeargeUpscaleModels</sub>, <sub>SeargeVAELoader</sub>
</details>

# TOP 36 - 40

<details><summary>Star History for TOP 36 - 40</summary><a href="https://api.star-history.com/svg?repos=banodoco/Steerable-Motion,wyrde/wyrde-comfyui-workflows,diStyApps/seait,rgthree/rgthree-comfy,BennyKok/comfyui-deploy&type=Date"><img src="https://api.star-history.com/svg?repos=banodoco/Steerable-Motion,wyrde/wyrde-comfyui-workflows,diStyApps/seait,rgthree/rgthree-comfy,BennyKok/comfyui-deploy&type=Date" alt="Star History Chart" width="500"></a></details>


## 36. banodoco/Steerable-Motion


<a href='https://github.com/banodoco/Steerable-Motion'>
<img src="https://avatars.githubusercontent.com/u/134059142?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/banodoco/Steerable-Motion

**Stars**: `728` | **Created at**: `2023-11-11` | **Last updated**: `2024-06-09` | **Tags**: `Custom Nodes` `Video`


A ComfyUI node for driving videos using batches of images.

## 37. wyrde/wyrde-comfyui-workflows


<a href='https://github.com/wyrde/wyrde-comfyui-workflows'>
<img src="https://avatars.githubusercontent.com/u/9657443?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/wyrde/wyrde-comfyui-workflows

**Stars**: `699` | **Created at**: `2023-04-03` | **Last updated**: `2024-06-09` | **Tags**: `Workflow Examples`


some wyrde workflows for comfyUI

## 38. diStyApps/seait


<a href='https://github.com/diStyApps/seait'>
<img src="https://avatars.githubusercontent.com/u/3084832?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/diStyApps/seait

**Stars**: `686` | **Created at**: `2023-04-01` | **Last updated**: `2024-06-07` | **Tags**: `Integration`


SEAIT is a user-friendly application that simplifies the installation process of AI-related projects

## 39. rgthree/rgthree-comfy


<a href='https://github.com/rgthree/rgthree-comfy'>
<img src="https://avatars.githubusercontent.com/u/476360?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/rgthree/rgthree-comfy

**Stars**: `657` | **Created at**: `2023-08-14` | **Last updated**: `2024-06-09` | **Tags**: `Custom Nodes`


Making ComfyUI more comfortable!
<details><summary>Included Nodes (0)?</summary>

 - Sorry, we can't get the node list for this project since it lacks conventional `NODE_CLASS_MAPPINGS` and doesn't have a `node_list.json` file to specify the node details according to [ComfyUI-Manager's support guide](https://github.com/ltdrdata/ComfyUI-Manager#custom-node-support-guide)</details>


## 40. BennyKok/comfyui-deploy


<a href='https://github.com/BennyKok/comfyui-deploy'>
<img src="https://avatars.githubusercontent.com/u/18395202?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/BennyKok/comfyui-deploy

**Stars**: `651` | **Created at**: `2023-12-08` | **Last updated**: `2024-06-09` | **Tags**: `Custom Nodes` `Integration`


An open source `vercel` like deployment platform for Comfy UI
<details><summary>Included Nodes (14)</summary>

 - <sub>ComfyDeployWebscoketImageInput</sub>, <sub>ComfyDeployWebscoketImageOutput</sub>, <sub>ComfyUIDeployExternalBoolean</sub>, <sub>ComfyUIDeployExternalCheckpoint</sub>, <sub>ComfyUIDeployExternalImage</sub>, <sub>ComfyUIDeployExternalImageAlpha</sub>, <sub>ComfyUIDeployExternalImageBatch</sub>, <sub>ComfyUIDeployExternalLora</sub>, <sub>ComfyUIDeployExternalNumber</sub>, <sub>ComfyUIDeployExternalNumberInt</sub>, <sub>ComfyUIDeployExternalNumberSlider</sub>, <sub>ComfyUIDeployExternalText</sub>, <sub>ComfyUIDeployExternalVid</sub>, <sub>ComfyUIDeployExternalVideo</sub>
</details>

# TOP 41 - 45

<details><summary>Star History for TOP 41 - 45</summary><a href="https://api.star-history.com/svg?repos=jags111/efficiency-nodes-comfyui,AlekPet/ComfyUI_Custom_Nodes_AlekPet,ArtVentureX/comfyui-animatediff,rvion/CushyStudio,ssitu/ComfyUI_UltimateSDUpscale&type=Date"><img src="https://api.star-history.com/svg?repos=jags111/efficiency-nodes-comfyui,AlekPet/ComfyUI_Custom_Nodes_AlekPet,ArtVentureX/comfyui-animatediff,rvion/CushyStudio,ssitu/ComfyUI_UltimateSDUpscale&type=Date" alt="Star History Chart" width="500"></a></details>


## 41. jags111/efficiency-nodes-comfyui


<a href='https://github.com/jags111/efficiency-nodes-comfyui'>
<img src="https://avatars.githubusercontent.com/u/5968619?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/jags111/efficiency-nodes-comfyui

**Stars**: `648` | **Created at**: `2023-08-31` | **Last updated**: `2024-06-09` | **Tags**: `Custom Nodes`


A collection of ComfyUI custom nodes.- Awesome smart way to work with nodes!
<details><summary>Included Nodes (39)</summary>

 - <sub>AnimateDiff Script</sub>, <sub>Apply ControlNet Stack</sub>
 - <sub>Control Net Stacker</sub>
 - <sub>Eff. Loader SDXL</sub>, <sub>Efficient Loader</sub>
 - <sub>HighRes-Fix Script</sub>
 - <sub>Image Overlay</sub>
 - <sub>Join XY Inputs of Same Type</sub>
 - <sub>KSampler (Efficient)</sub>, <sub>KSampler Adv. (Efficient)</sub>, <sub>KSampler SDXL (Eff.)</sub>
 - <sub>LatentUpscaler</sub>, <sub>LoRA Stack to String converter</sub>, <sub>LoRA Stacker</sub>
 - <sub>Manual XY Entry Info</sub>
 - <sub>NNLatentUpscale</sub>, <sub>Noise Control Script</sub>
 - <sub>Pack SDXL Tuple</sub>
 - <sub>Tiled Upscaler Script</sub>
 - <sub>Unpack SDXL Tuple</sub>
 - <sub>XY Input: Add/Return Noise</sub>, <sub>XY Input: Aesthetic Score</sub>, <sub>XY Input: CFG Scale</sub>, <sub>XY Input: Checkpoint</sub>, <sub>XY Input: Clip Skip</sub>, <sub>XY Input: Control Net</sub>, <sub>XY Input: Control Net Plot</sub>, <sub>XY Input: Denoise</sub>, <sub>XY Input: LoRA</sub>, <sub>XY Input: LoRA Plot</sub>, <sub>XY Input: LoRA Stacks</sub>, <sub>XY Input: Manual XY Entry</sub>, <sub>XY Input: Prompt S/R</sub>, <sub>XY Input: Refiner On/Off</sub>, <sub>XY Input: Sampler/Scheduler</sub>, <sub>XY Input: Seeds++ Batch</sub>, <sub>XY Input: Steps</sub>, <sub>XY Input: VAE</sub>, <sub>XY Plot</sub>
</details>


## 42. AlekPet/ComfyUI_Custom_Nodes_AlekPet


<a href='https://github.com/AlekPet/ComfyUI_Custom_Nodes_AlekPet'>
<img src="https://avatars.githubusercontent.com/u/25489996?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/AlekPet/ComfyUI_Custom_Nodes_AlekPet

**Stars**: `630` | **Created at**: `2023-05-10` | **Last updated**: `2024-06-08` | **Tags**: `Custom Nodes`


Custom nodes that extend the capabilities of Comfyui
<details><summary>Included Nodes (9)</summary>

 - <sub>ArgosTranslateCLIPTextEncodeNode</sub>, <sub>ArgosTranslateTextNode</sub>
 - <sub>DeepTranslatorCLIPTextEncodeNode</sub>, <sub>DeepTranslatorTextNode</sub>
 - <sub>GoogleTranslateCLIPTextEncodeNode</sub>, <sub>GoogleTranslateTextNode</sub>
 - <sub>PainterNode</sub>, <sub>PoseNode</sub>, <sub>PreviewTextNode</sub>
</details>


## 43. ArtVentureX/comfyui-animatediff


<a href='https://github.com/ArtVentureX/comfyui-animatediff'>
<img src="https://avatars.githubusercontent.com/u/133736036?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/ArtVentureX/comfyui-animatediff

**Stars**: `625` | **Created at**: `2023-07-22` | **Last updated**: `2024-06-08` | **Tags**: `Custom Nodes` `Video`


AnimateDiff for ComfyUI
<details><summary>Included Nodes (7)</summary>

 - <sub>AnimateDiffCombine</sub>, <sub>AnimateDiffLoraLoader</sub>, <sub>AnimateDiffModuleLoader</sub>, <sub>AnimateDiffSampler</sub>, <sub>AnimateDiffSlidingWindowOptions</sub>
 - <sub>ImageSizeAndBatchSize</sub>
 - <sub>LoadVideo</sub>
</details>


## 44. rvion/CushyStudio


<a href='https://github.com/rvion/CushyStudio'>
<img src="https://avatars.githubusercontent.com/u/2150990?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/rvion/CushyStudio

**Stars**: `601` | **Created at**: `2023-02-28` | **Last updated**: `2024-06-09` | **Tags**: `Integration`


🛋 The AI and Generative Art platform for everyone

## 45. ssitu/ComfyUI_UltimateSDUpscale


<a href='https://github.com/ssitu/ComfyUI_UltimateSDUpscale'>
<img src="https://avatars.githubusercontent.com/u/57548627?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/ssitu/ComfyUI_UltimateSDUpscale

**Stars**: `597` | **Created at**: `2023-05-16` | **Last updated**: `2024-06-07` | **Tags**: `Custom Nodes`


ComfyUI nodes for the Ultimate Stable Diffusion Upscale script by Coyote-A.
<details><summary>Included Nodes (2)</summary>

 - <sub>UltimateSDUpscale</sub>, <sub>UltimateSDUpscaleNoUpscale</sub>
</details>

# TOP 46 - 50

<details><summary>Star History for TOP 46 - 50</summary><a href="https://api.star-history.com/svg?repos=twri/sdxl_prompt_styler,LucianoCirino/efficiency-nodes-comfyui,ZHO-ZHO-ZHO/ComfyUI-Gemini,chflame163/ComfyUI_LayerStyle,fofr/cog-face-to-sticker&type=Date"><img src="https://api.star-history.com/svg?repos=twri/sdxl_prompt_styler,LucianoCirino/efficiency-nodes-comfyui,ZHO-ZHO-ZHO/ComfyUI-Gemini,chflame163/ComfyUI_LayerStyle,fofr/cog-face-to-sticker&type=Date" alt="Star History Chart" width="500"></a></details>


## 46. twri/sdxl_prompt_styler


<a href='https://github.com/twri/sdxl_prompt_styler'>
<img src="https://avatars.githubusercontent.com/u/4344671?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/twri/sdxl_prompt_styler

**Stars**: `592` | **Created at**: `2023-07-22` | **Last updated**: `2024-06-08` | **Tags**: `Custom Nodes`


Custom prompt styler node for SDXL in ComfyUI
<details><summary>Included Nodes (2)</summary>

 - <sub>SDXLPromptStyler</sub>, <sub>SDXLPromptStylerAdvanced</sub>
</details>


## 47. LucianoCirino/efficiency-nodes-comfyui


<a href='https://github.com/LucianoCirino/efficiency-nodes-comfyui'>
<img src="https://avatars.githubusercontent.com/u/112517630?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/LucianoCirino/efficiency-nodes-comfyui

**Stars**: `581` | **Created at**: `2023-04-06` | **Last updated**: `2024-06-08` | **Tags**: `Custom Nodes` `Deprecated`


A collection of ComfyUI custom nodes. ⚠️ WARNING: This repo is no longer maintained.

## 48. ZHO-ZHO-ZHO/ComfyUI-Gemini


<a href='https://github.com/ZHO-ZHO-ZHO/ComfyUI-Gemini'>
<img src="https://avatars.githubusercontent.com/u/140084057?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/ZHO-ZHO-ZHO/ComfyUI-Gemini

**Stars**: `577` | **Created at**: `2023-12-19` | **Last updated**: `2024-06-09` | **Tags**: `Custom Nodes` `LLM` `Chinese Language`


Using Gemini in ComfyUI
<details><summary>Included Nodes (12)</summary>

 - <sub>ConcatText_Zho</sub>
 - <sub>DisplayText_Zho</sub>
 - <sub>Gemini_15P_API_S_Advance_Zho</sub>, <sub>Gemini_15P_API_S_Chat_Advance_Zho</sub>, <sub>Gemini_API_Chat_Zho</sub>, <sub>Gemini_API_S_Chat_Zho</sub>, <sub>Gemini_API_S_Vsion_ImgURL_Zho</sub>, <sub>Gemini_API_S_Zho</sub>, <sub>Gemini_API_Vsion_ImgURL_Zho</sub>, <sub>Gemini_API_Zho</sub>, <sub>Gemini_File_API_S_Zho</sub>, <sub>Gemini_FileUpload_API_S_Zho</sub>
</details>


## 49. chflame163/ComfyUI_LayerStyle


<a href='https://github.com/chflame163/ComfyUI_LayerStyle'>
<img src="https://avatars.githubusercontent.com/u/130118553?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/chflame163/ComfyUI_LayerStyle

**Stars**: `574` | **Created at**: `2024-01-17` | **Last updated**: `2024-06-09` | **Tags**: `Custom Nodes`


A set of nodes for ComfyUI that can composite layer and mask to achieve Photoshop like functionality.
<details><summary>Included Nodes (126)</summary>

 - <sub>LayerColor: AutoAdjust</sub>, <sub>LayerColor: AutoBrightness</sub>, <sub>LayerColor: Brightness & Contrast</sub>, <sub>LayerColor: Color of Shadow & Highlight</sub>, <sub>LayerColor: ColorAdapter</sub>, <sub>LayerColor: ColorBalance</sub>, <sub>LayerColor: ColorTemperature</sub>, <sub>LayerColor: Exposure</sub>, <sub>LayerColor: Gamma</sub>, <sub>LayerColor: HSV</sub>, <sub>LayerColor: LAB</sub>, <sub>LayerColor: Levels</sub>, <sub>LayerColor: LUT Apply</sub>, <sub>LayerColor: RGB</sub>, <sub>LayerColor: YUV</sub>, <sub>LayerFilter: ChannelShake</sub>, <sub>LayerFilter: ColorMap</sub>, <sub>LayerFilter: Film</sub>, <sub>LayerFilter: GaussianBlur</sub>, <sub>LayerFilter: HDREffects</sub>, <sub>LayerFilter: LightLeak</sub>, <sub>LayerFilter: MotionBlur</sub>, <sub>LayerFilter: Sharp & Soft</sub>, <sub>LayerFilter: SkinBeauty</sub>, <sub>LayerFilter: SoftLight</sub>, <sub>LayerFilter: WaterColor</sub>, <sub>LayerMask: BiRefNetUltra</sub>, <sub>LayerMask: BlendIf Mask</sub>, <sub>LayerMask: CreateGradientMask</sub>, <sub>LayerMask: MaskBoxDetect</sub>, <sub>LayerMask: MaskByColor</sub>, <sub>LayerMask: MaskByDifferent</sub>, <sub>LayerMask: MaskEdgeShrink</sub>, <sub>LayerMask: MaskEdgeUltraDetail</sub>, <sub>LayerMask: MaskEdgeUltraDetail V2</sub>, <sub>LayerMask: MaskGradient</sub>, <sub>LayerMask: MaskGrow</sub>, <sub>LayerMask: MaskInvert</sub>, <sub>LayerMask: MaskMotionBlur</sub>, <sub>LayerMask: MaskPreview</sub>, <sub>LayerMask: MaskStroke</sub>, <sub>LayerMask: MediapipeFacialSegment</sub>, <sub>LayerMask: PersonMaskUltra</sub>, <sub>LayerMask: PersonMaskUltra V2</sub>, <sub>LayerMask: PixelSpread</sub>, <sub>LayerMask: RemBgUltra</sub>, <sub>LayerMask: RmBgUltra V2</sub>, <sub>LayerMask: SegformerB2ClothesUltra</sub>, <sub>LayerMask: SegmentAnythingUltra</sub>, <sub>LayerMask: SegmentAnythingUltra V2</sub>, <sub>LayerMask: Shadow & Highlight Mask</sub>, <sub>LayerMask: YoloV8Detect</sub>, <sub>LayerStyle: ColorOverlay</sub>, <sub>LayerStyle: ColorOverlay V2</sub>, <sub>LayerStyle: DropShadow</sub>, <sub>LayerStyle: DropShadow V2</sub>, <sub>LayerStyle: GradientOverlay</sub>, <sub>LayerStyle: GradientOverlay V2</sub>, <sub>LayerStyle: InnerGlow</sub>, <sub>LayerStyle: InnerGlow V2</sub>, <sub>LayerStyle: InnerShadow</sub>, <sub>LayerStyle: InnerShadow V2</sub>, <sub>LayerStyle: OuterGlow</sub>, <sub>LayerStyle: OuterGlow V2</sub>, <sub>LayerStyle: Stroke</sub>, <sub>LayerStyle: Stroke V2</sub>, <sub>LayerUtility: AddBlindWaterMark</sub>, <sub>LayerUtility: BatchSelector</sub>, <sub>LayerUtility: Boolean</sub>, <sub>LayerUtility: BooleanOperator</sub>, <sub>LayerUtility: ColorImage</sub>, <sub>LayerUtility: ColorImage V2</sub>, <sub>LayerUtility: ColorPicker</sub>, <sub>LayerUtility: CreateQRCode</sub>, <sub>LayerUtility: CropBoxResolve</sub>, <sub>LayerUtility: CropByMask</sub>, <sub>LayerUtility: CropByMask V2</sub>, <sub>LayerUtility: DecodeQRCode</sub>, <sub>LayerUtility: ExtendCanvas</sub>, <sub>LayerUtility: ExtendCanvasV2</sub>, <sub>LayerUtility: Float</sub>, <sub>LayerUtility: GetColorTone</sub>, <sub>LayerUtility: GetColorToneV2</sub>, <sub>LayerUtility: GetImageSize</sub>, <sub>LayerUtility: GradientImage</sub>, <sub>LayerUtility: GradientImage V2</sub>, <sub>LayerUtility: ImageAutoCrop</sub>, <sub>LayerUtility: ImageAutoCrop V2</sub>, <sub>LayerUtility: ImageBlend</sub>, <sub>LayerUtility: ImageBlend V2</sub>, <sub>LayerUtility: ImageBlendAdvance</sub>, <sub>LayerUtility: ImageBlendAdvance V2</sub>, <sub>LayerUtility: ImageChannelMerge</sub>, <sub>LayerUtility: ImageChannelSplit</sub>, <sub>LayerUtility: ImageCombineAlpha</sub>, <sub>LayerUtility: ImageHub</sub>, <sub>LayerUtility: ImageMaskScaleAs</sub>, <sub>LayerUtility: ImageOpacity</sub>, <sub>LayerUtility: ImageRemoveAlpha</sub>, <sub>LayerUtility: ImageRewardFilter</sub>, <sub>LayerUtility: ImageScaleByAspectRatio</sub>, <sub>LayerUtility: ImageScaleByAspectRatio V2</sub>, <sub>LayerUtility: ImageScaleRestore</sub>, <sub>LayerUtility: ImageScaleRestore V2</sub>, <sub>LayerUtility: ImageShift</sub>, <sub>LayerUtility: Integer</sub>, <sub>LayerUtility: LaMa</sub>, <sub>LayerUtility: LayerImageTransform</sub>, <sub>LayerUtility: LayerMaskTransform</sub>, <sub>LayerUtility: LoadPSD</sub>, <sub>LayerUtility: NumberCalculator</sub>, <sub>LayerUtility: PrintInfo</sub>, <sub>LayerUtility: PromptEmbellish</sub>, <sub>LayerUtility: PromptTagger</sub>, <sub>LayerUtility: PurgeVRAM</sub>, <sub>LayerUtility: QWenImage2Prompt</sub>, <sub>LayerUtility: RestoreCropBox</sub>, <sub>LayerUtility: RGB Value</sub>, <sub>LayerUtility: SaveImagePlus</sub>, <sub>LayerUtility: Seed</sub>, <sub>LayerUtility: ShowBlindWaterMark</sub>, <sub>LayerUtility: SimpleTextImage</sub>, <sub>LayerUtility: TextBox</sub>, <sub>LayerUtility: TextImage</sub>, <sub>LayerUtility: TextJoin</sub>, <sub>LayerUtility: XY to Percent</sub>
</details>


## 50. fofr/cog-face-to-sticker


<a href='https://github.com/fofr/cog-face-to-sticker'>
<img src="https://avatars.githubusercontent.com/u/319055?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/fofr/cog-face-to-sticker

**Stars**: `573` | **Created at**: `2024-02-28` | **Last updated**: `2024-06-08` | **Tags**: `Workflow Examples`


face-to-sticker
# TOP 51 - 55

<details><summary>Star History for TOP 51 - 55</summary><a href="https://api.star-history.com/svg?repos=space-nuko/ComfyBox,AIGODLIKE/ComfyUI-BlenderAI-node,ZHO-ZHO-ZHO/ComfyUI-BRIA_AI-RMBG,WASasquatch/comfyui-plugins,storyicon/comfyui_segment_anything&type=Date"><img src="https://api.star-history.com/svg?repos=space-nuko/ComfyBox,AIGODLIKE/ComfyUI-BlenderAI-node,ZHO-ZHO-ZHO/ComfyUI-BRIA_AI-RMBG,WASasquatch/comfyui-plugins,storyicon/comfyui_segment_anything&type=Date" alt="Star History Chart" width="500"></a></details>


## 51. space-nuko/ComfyBox


<a href='https://github.com/space-nuko/ComfyBox'>
<img src="https://avatars.githubusercontent.com/u/24979496?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/space-nuko/ComfyBox

**Stars**: `555` | **Created at**: `2023-04-04` | **Last updated**: `2024-06-05` | **Tags**: `Integration`


Customizable Stable Diffusion frontend for ComfyUI

## 52. AIGODLIKE/ComfyUI-BlenderAI-node


<a href='https://github.com/AIGODLIKE/ComfyUI-BlenderAI-node'>
<img src="https://avatars.githubusercontent.com/u/124877023?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/AIGODLIKE/ComfyUI-BlenderAI-node

**Stars**: `542` | **Created at**: `2023-04-24` | **Last updated**: `2024-06-09` | **Tags**: `Integration` `3D`


Used for AI model generation, next-generation Blender rendering engine, texture enhancement&generation (based on ComfyUI)

## 53. ZHO-ZHO-ZHO/ComfyUI-BRIA_AI-RMBG


<a href='https://github.com/ZHO-ZHO-ZHO/ComfyUI-BRIA_AI-RMBG'>
<img src="https://avatars.githubusercontent.com/u/140084057?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/ZHO-ZHO-ZHO/ComfyUI-BRIA_AI-RMBG

**Stars**: `540` | **Created at**: `2024-02-06` | **Last updated**: `2024-06-08` | **Tags**: `Custom Nodes` `Chinese Language`


Unofficial implementation of BRIA RMBG Model for ComfyUI
<details><summary>Included Nodes (2)</summary>

 - <sub>BRIA_RMBG_ModelLoader_Zho</sub>, <sub>BRIA_RMBG_Zho</sub>
</details>


## 54. WASasquatch/comfyui-plugins


<a href='https://github.com/WASasquatch/comfyui-plugins'>
<img src="https://avatars.githubusercontent.com/u/1151589?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/WASasquatch/comfyui-plugins

**Stars**: `524` | **Created at**: `2023-04-10` | **Last updated**: `2024-06-09` | **Tags**: `Resources`


Extensions, Custom Nodes, and other plugins for ComfyUI

## 55. storyicon/comfyui_segment_anything


<a href='https://github.com/storyicon/comfyui_segment_anything'>
<img src="https://avatars.githubusercontent.com/u/29772821?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/storyicon/comfyui_segment_anything

**Stars**: `489` | **Created at**: `2023-10-07` | **Last updated**: `2024-06-08` | **Tags**: `Custom Nodes`


Based on GroundingDino and SAM, use semantic strings to segment any element in an image. The comfyui version of sd-webui-segment-anything.
<details><summary>Included Nodes (5)</summary>

 - <sub>GroundingDinoModelLoader (segment anything)</sub>, <sub>GroundingDinoSAMSegment (segment anything)</sub>
 - <sub>InvertMask (segment anything)</sub>, <sub>IsMaskEmpty</sub>
 - <sub>SAMModelLoader (segment anything)</sub>
</details>

# TOP 56 - 60

<details><summary>Star History for TOP 56 - 60</summary><a href="https://api.star-history.com/svg?repos=mrhan1993/Fooocus-API,yolain/ComfyUI-Easy-Use,Suzie1/ComfyUI_Comfyroll_CustomNodes,AlexanderDzhoganov/ComfyTextures,ModelSurge/sd-webui-comfyui&type=Date"><img src="https://api.star-history.com/svg?repos=mrhan1993/Fooocus-API,yolain/ComfyUI-Easy-Use,Suzie1/ComfyUI_Comfyroll_CustomNodes,AlexanderDzhoganov/ComfyTextures,ModelSurge/sd-webui-comfyui&type=Date" alt="Star History Chart" width="500"></a></details>


## 56. mrhan1993/Fooocus-API


<a href='https://github.com/mrhan1993/Fooocus-API'>
<img src="https://avatars.githubusercontent.com/u/50648276?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/mrhan1993/Fooocus-API

**Stars**: `476` | **Created at**: `2023-09-19` | **Last updated**: `2024-06-09` | **Tags**: `Integration`


FastAPI powered API for Fooocus

## 57. yolain/ComfyUI-Easy-Use


<a href='https://github.com/yolain/ComfyUI-Easy-Use'>
<img src="https://avatars.githubusercontent.com/u/73304135?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/yolain/ComfyUI-Easy-Use

**Stars**: `454` | **Created at**: `2023-12-10` | **Last updated**: `2024-06-09` | **Tags**: `Custom Nodes` `Chinese Language`


In order to make it easier to use the ComfyUI, I have made some optimizations and integrations to some commonly used nodes.
<details><summary>Included Nodes (142)</summary>

 - <sub>dynamicThresholdingFull</sub>
 - <sub>easy a1111Loader</sub>, <sub>easy applyBrushNet</sub>, <sub>easy applyFooocusInpaint</sub>, <sub>easy applyInpaint</sub>, <sub>easy applyPowerPaint</sub>, <sub>easy boolean</sub>, <sub>easy cascadeKSampler</sub>, <sub>easy cascadeLoader</sub>, <sub>easy ckptNames</sub>, <sub>easy cleanGpuUsed</sub>, <sub>easy clearCacheAll</sub>, <sub>easy clearCacheKey</sub>, <sub>easy comfyLoader</sub>, <sub>easy compare</sub>, <sub>easy controlnetLoader</sub>, <sub>easy controlnetLoaderADV</sub>, <sub>easy controlnetNames</sub>, <sub>easy controlnetStack</sub>, <sub>easy convertAnything</sub>, <sub>easy detailerFix</sub>, <sub>easy dynamiCrafterLoader</sub>, <sub>easy float</sub>, <sub>easy fullCascadeKSampler</sub>, <sub>easy fullkSampler</sub>, <sub>easy fullLoader</sub>, <sub>easy globalSeed</sub>, <sub>easy hiresFix</sub>, <sub>easy humanSegmentation</sub>, <sub>easy icLightApply</sub>, <sub>easy if</sub>, <sub>easy imageChooser</sub>, <sub>easy imageColorMatch</sub>, <sub>easy imageConcat</sub>, <sub>easy imageCount</sub>, <sub>easy imageCropFromMask</sub>, <sub>easy imageDetailTransfer</sub>, <sub>easy imageInsetCrop</sub>, <sub>easy imageInterrogator</sub>, <sub>easy imagePixelPerfect</sub>, <sub>easy imageRatio</sub>, <sub>easy imageRemBg</sub>, <sub>easy imageSave</sub>, <sub>easy imageScaleDown</sub>, <sub>easy imageScaleDownBy</sub>, <sub>easy imageScaleDownToSize</sub>, <sub>easy imageSize</sub>, <sub>easy imageSizeByLongerSide</sub>, <sub>easy imageSizeBySide</sub>, <sub>easy imageSplitGrid</sub>, <sub>easy imageSplitList</sub>, <sub>easy imagesSplitImage</sub>, <sub>easy imageSwitch</sub>, <sub>easy imageToBase64</sub>, <sub>easy imageToMask</sub>, <sub>easy imageUncropFromBBOX</sub>, <sub>easy injectNoiseToLatent</sub>, <sub>easy instantIDApply</sub>, <sub>easy instantIDApplyADV</sub>, <sub>easy int</sub>, <sub>easy ipadapterApply</sub>, <sub>easy ipadapterApplyADV</sub>, <sub>easy ipadapterApplyEmbeds</sub>, <sub>easy ipadapterApplyEncoder</sub>, <sub>easy ipadapterApplyFromParams</sub>, <sub>easy ipadapterApplyRegional</sub>, <sub>easy ipadapterStyleComposition</sub>, <sub>easy isSDXL</sub>, <sub>easy joinImageBatch</sub>, <sub>easy kSampler</sub>, <sub>easy kSamplerDownscaleUnet</sub>, <sub>easy kSamplerInpainting</sub>, <sub>easy kSamplerLayerDiffusion</sub>, <sub>easy kSamplerSDTurbo</sub>, <sub>easy kSamplerTiled</sub>, <sub>easy latentCompositeMaskedWithCond</sub>, <sub>easy latentNoisy</sub>, <sub>easy LLLiteLoader</sub>, <sub>easy loadImageBase64</sub>, <sub>easy loraStack</sub>, <sub>easy negative</sub>, <sub>easy pipeBatchIndex</sub>, <sub>easy pipeEdit</sub>, <sub>easy pipeIn</sub>, <sub>easy pipeOut</sub>, <sub>easy pipeToBasicPipe</sub>, <sub>easy portraitMaster</sub>, <sub>easy poseEditor</sub>, <sub>easy positive</sub>, <sub>easy preDetailerFix</sub>, <sub>easy preMaskDetailerFix</sub>, <sub>easy preSampling</sub>, <sub>easy preSamplingAdvanced</sub>, <sub>easy preSamplingCascade</sub>, <sub>easy preSamplingCustom</sub>, <sub>easy preSamplingDynamicCFG</sub>, <sub>easy preSamplingLayerDiffusion</sub>, <sub>easy preSamplingLayerDiffusionADDTL</sub>, <sub>easy preSamplingNoiseIn</sub>, <sub>easy preSamplingSdTurbo</sub>, <sub>easy prompt</sub>, <sub>easy promptConcat</sub>, <sub>easy promptLine</sub>, <sub>easy promptList</sub>, <sub>easy promptReplace</sub>, <sub>easy rangeFloat</sub>, <sub>easy rangeInt</sub>, <sub>easy removeLocalImage</sub>, <sub>easy samLoaderPipe</sub>, <sub>easy seed</sub>, <sub>easy showAnything</sub>, <sub>easy showLoaderSettingsNames</sub>, <sub>easy showSpentTime</sub>, <sub>easy showTensorShape</sub>, <sub>easy stableDiffusion3API</sub>, <sub>easy string</sub>, <sub>easy styleAlignedBatchAlign</sub>, <sub>easy stylesSelector</sub>, <sub>easy sv3dLoader</sub>, <sub>easy svdLoader</sub>, <sub>easy textSwitch</sub>, <sub>easy ultralyticsDetectorPipe</sub>, <sub>easy unSampler</sub>, <sub>easy wildcards</sub>, <sub>easy xyAny</sub>, <sub>easy XYInputs: CFG Scale</sub>, <sub>easy XYInputs: Checkpoint</sub>, <sub>easy XYInputs: ControlNet</sub>, <sub>easy XYInputs: Denoise</sub>, <sub>easy XYInputs: Lora</sub>, <sub>easy XYInputs: ModelMergeBlocks</sub>, <sub>easy XYInputs: NegativeCond</sub>, <sub>easy XYInputs: NegativeCondList</sub>, <sub>easy XYInputs: PositiveCond</sub>, <sub>easy XYInputs: PositiveCondList</sub>, <sub>easy XYInputs: PromptSR</sub>, <sub>easy XYInputs: Sampler/Scheduler</sub>, <sub>easy XYInputs: Seeds++ Batch</sub>, <sub>easy XYInputs: Steps</sub>, <sub>easy XYPlot</sub>, <sub>easy XYPlotAdvanced</sub>, <sub>easy zero123Loader</sub>
</details>


## 58. Suzie1/ComfyUI_Comfyroll_CustomNodes


<a href='https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes'>
<img src="https://avatars.githubusercontent.com/u/42118269?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes

**Stars**: `453` | **Created at**: `2023-06-10` | **Last updated**: `2024-06-07` | **Tags**: `Custom Nodes`


Custom nodes for SDXL and SD1.5 including Multi-ControlNet, LoRA, Aspect Ratio, Process Switches, and many more nodes.
<details><summary>Included Nodes (208)</summary>

 - <sub>CR 8 Channel In</sub>, <sub>CR 8 Channel Out</sub>, <sub>CR Apply ControlNet</sub>, <sub>CR Apply LoRA Stack</sub>, <sub>CR Apply Model Merge</sub>, <sub>CR Apply Multi Upscale</sub>, <sub>CR Apply Multi-ControlNet</sub>, <sub>CR Arabic Text RTL</sub>, <sub>CR Aspect Ratio</sub>, <sub>CR Aspect Ratio Banners</sub>, <sub>CR Aspect Ratio SDXL</sub>, <sub>CR Aspect Ratio Social Media</sub>, <sub>CR Batch Images From List</sub>, <sub>CR Batch Process Switch</sub>, <sub>CR Binary Pattern</sub>, <sub>CR Binary To Bit List</sub>, <sub>CR Bit Schedule</sub>, <sub>CR Central Schedule</sub>, <sub>CR Checker Pattern</sub>, <sub>CR Clamp Value</sub>, <sub>CR Clip Input Switch</sub>, <sub>CR Color Bars</sub>, <sub>CR Color Gradient</sub>, <sub>CR Color Panel</sub>, <sub>CR Color Tint</sub>, <sub>CR Combine Prompt</sub>, <sub>CR Combine Schedules</sub>, <sub>CR Comic Panel Templates</sub>, <sub>CR Composite Text</sub>, <sub>CR Conditioning Input Switch</sub>, <sub>CR Conditioning Mixer</sub>, <sub>CR ControlNet Input Switch</sub>, <sub>CR Current Frame</sub>, <sub>CR Cycle Images</sub>, <sub>CR Cycle Images Simple</sub>, <sub>CR Cycle LoRAs</sub>, <sub>CR Cycle Models</sub>, <sub>CR Cycle Text</sub>, <sub>CR Cycle Text Simple</sub>, <sub>CR Data Bus In</sub>, <sub>CR Data Bus Out</sub>, <sub>CR Debatch Frames</sub>, <sub>CR Diamond Panel</sub>, <sub>CR Draw Perspective Text</sub>, <sub>CR Draw Pie</sub>, <sub>CR Draw Shape</sub>, <sub>CR Draw Text</sub>, <sub>CR Encode Scheduled Prompts</sub>, <sub>CR Feathered Border</sub>, <sub>CR Float Range List</sub>, <sub>CR Float To Integer</sub>, <sub>CR Float To String</sub>, <sub>CR Font File List</sub>, <sub>CR Get Parameter From Prompt</sub>, <sub>CR Gradient Float</sub>, <sub>CR Gradient Integer</sub>, <sub>CR Half Drop Panel</sub>, <sub>CR Halftone Filter</sub>, <sub>CR Halftone Grid</sub>, <sub>CR Hires Fix Process Switch</sub>, <sub>CR Image Border</sub>, <sub>CR Image Grid Panel</sub>, <sub>CR Image Input Switch</sub>, <sub>CR Image Input Switch (4 way)</sub>, <sub>CR Image List</sub>, <sub>CR Image List Simple</sub>, <sub>CR Image Output</sub>, <sub>CR Image Panel</sub>, <sub>CR Image Pipe Edit</sub>, <sub>CR Image Pipe In</sub>, <sub>CR Image Pipe Out</sub>, <sub>CR Image Size</sub>, <sub>CR Img2Img Process Switch</sub>, <sub>CR Increment Float</sub>, <sub>CR Increment Integer</sub>, <sub>CR Index</sub>, <sub>CR Index Increment</sub>, <sub>CR Index Multiply</sub>, <sub>CR Index Reset</sub>, <sub>CR Input Text List</sub>, <sub>CR Integer Multiple</sub>, <sub>CR Integer Range List</sub>, <sub>CR Integer To String</sub>, <sub>CR Interpolate Latents</sub>, <sub>CR Intertwine Lists</sub>, <sub>CR Keyframe List</sub>, <sub>CR Latent Batch Size</sub>, <sub>CR Latent Input Switch</sub>, <sub>CR Load Animation Frames</sub>, <sub>CR Load Flow Frames</sub>, <sub>CR Load GIF As List</sub>, <sub>CR Load Image List</sub>, <sub>CR Load Image List Plus</sub>, <sub>CR Load LoRA</sub>, <sub>CR Load Prompt Style</sub>, <sub>CR Load Schedule From File</sub>, <sub>CR Load Scheduled ControlNets</sub>, <sub>CR Load Scheduled LoRAs</sub>, <sub>CR Load Scheduled Models</sub>, <sub>CR Load Text List</sub>, <sub>CR LoRA List</sub>, <sub>CR LoRA Stack</sub>, <sub>CR Mask Text</sub>, <sub>CR Math Operation</sub>, <sub>CR Model Input Switch</sub>, <sub>CR Model List</sub>, <sub>CR Model Merge Stack</sub>, <sub>CR Module Input</sub>, <sub>CR Module Output</sub>, <sub>CR Module Pipe Loader</sub>, <sub>CR Multi Upscale Stack</sub>, <sub>CR Multi-ControlNet Stack</sub>, <sub>CR Multiline Text</sub>, <sub>CR Output Flow Frames</sub>, <sub>CR Output Schedule To File</sub>, <sub>CR Overlay Text</sub>, <sub>CR Overlay Transparent Image</sub>, <sub>CR Page Layout</sub>, <sub>CR Pipe Switch</sub>, <sub>CR Polygons</sub>, <sub>CR Prompt List</sub>, <sub>CR Prompt List Keyframes</sub>, <sub>CR Prompt Scheduler</sub>, <sub>CR Prompt Text</sub>, <sub>CR Radial Gradient</sub>, <sub>CR Random Hex Color</sub>, <sub>CR Random LoRA Stack</sub>, <sub>CR Random Multiline Colors</sub>, <sub>CR Random Multiline Values</sub>, <sub>CR Random Panel Codes</sub>, <sub>CR Random RGB</sub>, <sub>CR Random RGB Gradient</sub>, <sub>CR Random Shape Pattern</sub>, <sub>CR Random Weight LoRA</sub>, <sub>CR Repeater</sub>, <sub>CR Save Text To File</sub>, <sub>CR Schedule Input Switch</sub>, <sub>CR Schedule To ScheduleList</sub>, <sub>CR SD1.5 Aspect Ratio</sub>, <sub>CR SDXL Aspect Ratio</sub>, <sub>CR SDXL Base Prompt Encoder</sub>, <sub>CR SDXL Prompt Mix Presets</sub>, <sub>CR SDXL Prompt Mixer</sub>, <sub>CR SDXL Style Text</sub>, <sub>CR Seamless Checker</sub>, <sub>CR Seed</sub>, <sub>CR Seed to Int</sub>, <sub>CR Select Font</sub>, <sub>CR Select ISO Size</sub>, <sub>CR Select Model</sub>, <sub>CR Select Resize Method</sub>, <sub>CR Set Switch From String</sub>, <sub>CR Set Value On Binary</sub>, <sub>CR Set Value On Boolean</sub>, <sub>CR Set Value on String</sub>, <sub>CR Simple Banner</sub>, <sub>CR Simple Binary Pattern</sub>, <sub>CR Simple Binary Pattern Simple</sub>, <sub>CR Simple Image Compare</sub>, <sub>CR Simple List</sub>, <sub>CR Simple Meme Template</sub>, <sub>CR Simple Prompt List</sub>, <sub>CR Simple Prompt List Keyframes</sub>, <sub>CR Simple Prompt Scheduler</sub>, <sub>CR Simple Schedule</sub>, <sub>CR Simple Text Panel</sub>, <sub>CR Simple Text Scheduler</sub>, <sub>CR Simple Text Watermark</sub>, <sub>CR Simple Titles</sub>, <sub>CR Simple Value Scheduler</sub>, <sub>CR Split String</sub>, <sub>CR Starburst Colors</sub>, <sub>CR Starburst Lines</sub>, <sub>CR String To Boolean</sub>, <sub>CR String To Combo</sub>, <sub>CR String To Number</sub>, <sub>CR Style Bars</sub>, <sub>CR Switch Model and CLIP</sub>, <sub>CR Text</sub>, <sub>CR Text Blacklist</sub>, <sub>CR Text Concatenate</sub>, <sub>CR Text Cycler</sub>, <sub>CR Text Input Switch</sub>, <sub>CR Text Input Switch (4 way)</sub>, <sub>CR Text Length</sub>, <sub>CR Text List</sub>, <sub>CR Text List Simple</sub>, <sub>CR Text List To String</sub>, <sub>CR Text Operation</sub>, <sub>CR Text Replace</sub>, <sub>CR Text Scheduler</sub>, <sub>CR Thumbnail Preview</sub>, <sub>CR Trigger</sub>, <sub>CR Upscale Image</sub>, <sub>CR VAE Decode</sub>, <sub>CR VAE Input Switch</sub>, <sub>CR Value</sub>, <sub>CR Value Cycler</sub>, <sub>CR Value Scheduler</sub>, <sub>CR Vignette Filter</sub>, <sub>CR XY From Folder</sub>, <sub>CR XY Index</sub>, <sub>CR XY Interpolate</sub>, <sub>CR XY List</sub>, <sub>CR XY Product</sub>, <sub>CR XY Save Grid Image</sub>, <sub>CR XYZ Index</sub>, <sub>CR_Aspect Ratio For Print</sub>
</details>


## 59. AlexanderDzhoganov/ComfyTextures


<a href='https://github.com/AlexanderDzhoganov/ComfyTextures'>
<img src="https://avatars.githubusercontent.com/u/855464?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/AlexanderDzhoganov/ComfyTextures

**Stars**: `453` | **Created at**: `2024-01-25` | **Last updated**: `2024-06-07` | **Tags**: `Integration` `3D`


Unreal Engine ⚔️ ComfyUI - Automatic texturing using generative diffusion models 

## 60. ModelSurge/sd-webui-comfyui


<a href='https://github.com/ModelSurge/sd-webui-comfyui'>
<img src="https://avatars.githubusercontent.com/u/120546502?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/ModelSurge/sd-webui-comfyui

**Stars**: `450` | **Created at**: `2023-03-19` | **Last updated**: `2024-06-07` | **Tags**: `Integration`


An extension to integrate ComfyUI workflows into the Webui's pipeline
# TOP 61 - 65

<details><summary>Star History for TOP 61 - 65</summary><a href="https://api.star-history.com/svg?repos=crystian/ComfyUI-Crystools,ZHO-ZHO-ZHO/ComfyUI-YoloWorld-EfficientSAM,ltdrdata/ComfyUI-extension-tutorials,xingren23/ComfyFlowApp,MrForExample/ComfyUI-AnimateAnyone-Evolved&type=Date"><img src="https://api.star-history.com/svg?repos=crystian/ComfyUI-Crystools,ZHO-ZHO-ZHO/ComfyUI-YoloWorld-EfficientSAM,ltdrdata/ComfyUI-extension-tutorials,xingren23/ComfyFlowApp,MrForExample/ComfyUI-AnimateAnyone-Evolved&type=Date" alt="Star History Chart" width="500"></a></details>


## 61. crystian/ComfyUI-Crystools


<a href='https://github.com/crystian/ComfyUI-Crystools'>
<img src="https://avatars.githubusercontent.com/u/3886806?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/crystian/ComfyUI-Crystools

**Stars**: `443` | **Created at**: `2023-12-23` | **Last updated**: `2024-06-08` | **Tags**: `Management`


A powerful set of tools for ComfyUI
<details><summary>Included Nodes (0)?</summary>

 - Sorry, we can't get the node list for this project since it lacks conventional `NODE_CLASS_MAPPINGS` and doesn't have a `node_list.json` file to specify the node details according to [ComfyUI-Manager's support guide](https://github.com/ltdrdata/ComfyUI-Manager#custom-node-support-guide)</details>


## 62. ZHO-ZHO-ZHO/ComfyUI-YoloWorld-EfficientSAM


<a href='https://github.com/ZHO-ZHO-ZHO/ComfyUI-YoloWorld-EfficientSAM'>
<img src="https://avatars.githubusercontent.com/u/140084057?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/ZHO-ZHO-ZHO/ComfyUI-YoloWorld-EfficientSAM

**Stars**: `433` | **Created at**: `2024-02-19` | **Last updated**: `2024-06-07` | **Tags**: `Custom Nodes` `Chinese Language`


Unofficial implementation of  YOLO-World + EfficientSAM for ComfyUI
<details><summary>Included Nodes (4)</summary>

 - <sub>ESAM_ModelLoader_Zho</sub>
 - <sub>Yoloworld_ESAM_DetectorProvider_Zho</sub>, <sub>Yoloworld_ESAM_Zho</sub>, <sub>Yoloworld_ModelLoader_Zho</sub>
</details>


## 63. ltdrdata/ComfyUI-extension-tutorials


<a href='https://github.com/ltdrdata/ComfyUI-extension-tutorials'>
<img src="https://avatars.githubusercontent.com/u/128333288?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/ltdrdata/ComfyUI-extension-tutorials

**Stars**: `432` | **Created at**: `2023-05-04` | **Last updated**: `2024-06-08` | **Tags**: `Tutorials`


None

## 64. xingren23/ComfyFlowApp


<a href='https://github.com/xingren23/ComfyFlowApp'>
<img src="https://avatars.githubusercontent.com/u/3837202?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/xingren23/ComfyFlowApp

**Stars**: `428` | **Created at**: `2023-10-08` | **Last updated**: `2024-06-08` | **Tags**: `Integration`


From comfyui workflow to web app, in seconds

## 65. MrForExample/ComfyUI-AnimateAnyone-Evolved


<a href='https://github.com/MrForExample/ComfyUI-AnimateAnyone-Evolved'>
<img src="https://avatars.githubusercontent.com/u/62230687?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/MrForExample/ComfyUI-AnimateAnyone-Evolved

**Stars**: `428` | **Created at**: `2024-01-18` | **Last updated**: `2024-06-06` | **Tags**: `Custom Nodes` `Video`


Improved AnimateAnyone implementation that allows you to use the opse image sequence and reference image to generate stylized video 
<details><summary>Included Nodes (0)?</summary>

 - Sorry, we can't get the node list for this project since it lacks conventional `NODE_CLASS_MAPPINGS` and doesn't have a `node_list.json` file to specify the node details according to [ComfyUI-Manager's support guide](https://github.com/ltdrdata/ComfyUI-Manager#custom-node-support-guide)</details>

# TOP 66 - 70

<details><summary>Star History for TOP 66 - 70</summary><a href="https://api.star-history.com/svg?repos=toyxyz/ComfyUI_toyxyz_test_nodes,kijai/ComfyUI-DynamiCrafterWrapper,SytanSD/Sytan-SDXL-ComfyUI,talesofai/comfyui-browser,fofr/cog-consistent-character&type=Date"><img src="https://api.star-history.com/svg?repos=toyxyz/ComfyUI_toyxyz_test_nodes,kijai/ComfyUI-DynamiCrafterWrapper,SytanSD/Sytan-SDXL-ComfyUI,talesofai/comfyui-browser,fofr/cog-consistent-character&type=Date" alt="Star History Chart" width="500"></a></details>


## 66. toyxyz/ComfyUI_toyxyz_test_nodes


<a href='https://github.com/toyxyz/ComfyUI_toyxyz_test_nodes'>
<img src="https://avatars.githubusercontent.com/u/8006000?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/toyxyz/ComfyUI_toyxyz_test_nodes

**Stars**: `427` | **Created at**: `2023-11-22` | **Last updated**: `2024-06-07` | **Tags**: `Custom Nodes` `3D`


Custom node and script for sending webcam to ComfyUI
<details><summary>Included Nodes (5)</summary>

 - <sub>CaptureWebcam</sub>
 - <sub>ImageResize_Padding</sub>
 - <sub>LatentDelay</sub>, <sub>LoadWebcamImage</sub>
 - <sub>SaveImagetoPath</sub>
</details>


## 67. kijai/ComfyUI-DynamiCrafterWrapper


<a href='https://github.com/kijai/ComfyUI-DynamiCrafterWrapper'>
<img src="https://avatars.githubusercontent.com/u/40791699?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/kijai/ComfyUI-DynamiCrafterWrapper

**Stars**: `427` | **Created at**: `2024-03-15` | **Last updated**: `2024-06-09` | **Tags**: `Custom Nodes` `Video`


Wrapper to use DynamiCrafter models in ComfyUI
<details><summary>Included Nodes (8)</summary>

 - <sub>DownloadAndLoadCLIPModel</sub>, <sub>DownloadAndLoadCLIPVisionModel</sub>, <sub>DownloadAndLoadDynamiCrafterModel</sub>, <sub>DynamiCrafterBatchInterpolation</sub>, <sub>DynamiCrafterI2V</sub>, <sub>DynamiCrafterModelLoader</sub>
 - <sub>ToonCrafterDecode</sub>, <sub>ToonCrafterInterpolation</sub>
</details>


## 68. SytanSD/Sytan-SDXL-ComfyUI


<a href='https://github.com/SytanSD/Sytan-SDXL-ComfyUI'>
<img src="https://avatars.githubusercontent.com/u/122675732?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/SytanSD/Sytan-SDXL-ComfyUI

**Stars**: `408` | **Created at**: `2023-07-09` | **Last updated**: `2024-06-07` | **Tags**: `Workflow Examples`


A hub dedicated to development and upkeep of the Sytan SDXL workflow for ComfyUI

## 69. talesofai/comfyui-browser


<a href='https://github.com/talesofai/comfyui-browser'>
<img src="https://avatars.githubusercontent.com/u/120728204?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/talesofai/comfyui-browser

**Stars**: `402` | **Created at**: `2023-11-26` | **Last updated**: `2024-06-08` | **Tags**: `Management` `Custom Nodes`


An image/video/workflow browser and manager for ComfyUI.
<details><summary>Included Nodes (5)</summary>

 - <sub>DifyTextGenerator //Browser</sub>
 - <sub>LoadImageByUrl //Browser</sub>
 - <sub>SelectInputs //Browser</sub>
 - <sub>UploadToRemote //Browser</sub>
 - <sub>XyzPlot //Browser</sub>
</details>


## 70. fofr/cog-consistent-character


<a href='https://github.com/fofr/cog-consistent-character'>
<img src="https://avatars.githubusercontent.com/u/319055?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/fofr/cog-consistent-character

**Stars**: `399` | **Created at**: `2024-05-30` | **Last updated**: `2024-06-09` | **Tags**: `Workflow Examples`


Create images of a given character in different poses
# TOP 71 - 75

<details><summary>Star History for TOP 71 - 75</summary><a href="https://api.star-history.com/svg?repos=pythongosssss/ComfyUI-WD14-Tagger,Kosinkadink/ComfyUI-Advanced-ControlNet,frankchieng/ComfyUI_MagicClothing,Acly/comfyui-inpaint-nodes,cubiq/PuLID_ComfyUI&type=Date"><img src="https://api.star-history.com/svg?repos=pythongosssss/ComfyUI-WD14-Tagger,Kosinkadink/ComfyUI-Advanced-ControlNet,frankchieng/ComfyUI_MagicClothing,Acly/comfyui-inpaint-nodes,cubiq/PuLID_ComfyUI&type=Date" alt="Star History Chart" width="500"></a></details>


## 71. pythongosssss/ComfyUI-WD14-Tagger


<a href='https://github.com/pythongosssss/ComfyUI-WD14-Tagger'>
<img src="https://avatars.githubusercontent.com/u/125205205?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/pythongosssss/ComfyUI-WD14-Tagger

**Stars**: `398` | **Created at**: `2023-05-11` | **Last updated**: `2024-06-08` | **Tags**: `Custom Nodes`


A ComfyUI extension allowing for the interrogation of booru tags from images.
<details><summary>Included Nodes (1)</summary>

 - <sub>WD14Tagger|pysssss</sub>
</details>


## 72. Kosinkadink/ComfyUI-Advanced-ControlNet


<a href='https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet'>
<img src="https://avatars.githubusercontent.com/u/7365912?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet

**Stars**: `397` | **Created at**: `2023-08-01` | **Last updated**: `2024-06-07` | **Tags**: `Custom Nodes`


ControlNet scheduling and masking nodes with sliding context support
<details><summary>Included Nodes (28)</summary>

 - [ACN_AdvancedControlNetApply🌟](node_examples/ACN_AdvancedControlNetApply.md), <sub>ACN_ControlNetLoaderWithLoraAdvanced</sub>, <sub>ACN_DefaultUniversalWeights</sub>, <sub>[ACN_ReferenceControlNet](node_examples/ACN_ReferenceControlNet.md)</sub>, <sub>ACN_ReferenceControlNetFinetune</sub>, <sub>ACN_ReferencePreprocessor</sub>, <sub>[ACN_SparseCtrlIndexMethodNode](node_examples/ACN_SparseCtrlIndexMethodNode.md)</sub>, <sub>[ACN_SparseCtrlLoaderAdvanced](node_examples/ACN_SparseCtrlLoaderAdvanced.md)</sub>, <sub>ACN_SparseCtrlMergedLoaderAdvanced</sub>, <sub>[ACN_SparseCtrlRGBPreprocessor](node_examples/ACN_SparseCtrlRGBPreprocessor.md)</sub>, <sub>[ACN_SparseCtrlSpreadMethodNode](node_examples/ACN_SparseCtrlSpreadMethodNode.md)</sub>, <sub>ACN_SparseCtrlWeightExtras</sub>, <sub>ACN_TimestepKeyframeFromStrengthList</sub>, <sub>ACN_TimestepKeyframeInterpolation</sub>
 - <sub>ControlNetLoaderAdvanced</sub>, <sub>CustomControlNetWeights</sub>, <sub>CustomT2IAdapterWeights</sub>
 - <sub>DiffControlNetLoaderAdvanced</sub>
 - <sub>LatentKeyframe</sub>, <sub>LatentKeyframeBatchedGroup</sub>, <sub>LatentKeyframeGroup</sub>, <sub>LatentKeyframeTiming</sub>, <sub>LoadImagesFromDirectory</sub>
 - <sub>ScaledSoftControlNetWeights</sub>, <sub>ScaledSoftMaskedUniversalWeights</sub>, <sub>SoftControlNetWeights</sub>, <sub>SoftT2IAdapterWeights</sub>
 - <sub>TimestepKeyframe</sub>
</details>


## 73. frankchieng/ComfyUI_MagicClothing


<a href='https://github.com/frankchieng/ComfyUI_MagicClothing'>
<img src="https://avatars.githubusercontent.com/u/130369523?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/frankchieng/ComfyUI_MagicClothing

**Stars**: `396` | **Created at**: `2024-04-17` | **Last updated**: `2024-06-08` | **Tags**: `Custom Nodes`


unofficial implementation of Comfyui magic clothing
<details><summary>Included Nodes (3)</summary>

 - <sub>MagicClothing_Animatediff</sub>, <sub>MagicClothing_Generate</sub>, <sub>MagicClothing_Inpainting</sub>
</details>


## 74. Acly/comfyui-inpaint-nodes


<a href='https://github.com/Acly/comfyui-inpaint-nodes'>
<img src="https://avatars.githubusercontent.com/u/6485914?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/Acly/comfyui-inpaint-nodes

**Stars**: `393` | **Created at**: `2024-01-24` | **Last updated**: `2024-06-09` | **Tags**: `Custom Nodes`


Nodes for better inpainting with ComfyUI: Fooocus inpaint model for SDXL, LaMa, MAT, and various other tools for pre-filling inpaint & outpaint areas.
<details><summary>Included Nodes (8)</summary>

 - <sub>INPAINT_ApplyFooocusInpaint</sub>, <sub>INPAINT_DenoiseToCompositingMask</sub>, <sub>INPAINT_InpaintWithModel</sub>, <sub>INPAINT_LoadFooocusInpaint</sub>, <sub>INPAINT_LoadInpaintModel</sub>, <sub>INPAINT_MaskedBlur</sub>, <sub>INPAINT_MaskedFill</sub>, <sub>INPAINT_VAEEncodeInpaintConditioning</sub>
</details>


## 75. cubiq/PuLID_ComfyUI


<a href='https://github.com/cubiq/PuLID_ComfyUI'>
<img src="https://avatars.githubusercontent.com/u/427614?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/cubiq/PuLID_ComfyUI

**Stars**: `380` | **Created at**: `2024-05-08` | **Last updated**: `2024-06-09` | **Tags**: `Custom Nodes`


PuLID native implementation for ComfyUI
<details><summary>Included Nodes (5)</summary>

 - <sub>ApplyPulid</sub>, <sub>ApplyPulidAdvanced</sub>
 - <sub>PulidEvaClipLoader</sub>, <sub>PulidInsightFaceLoader</sub>, <sub>PulidModelLoader</sub>
</details>

# TOP 76 - 80

<details><summary>Star History for TOP 76 - 80</summary><a href="https://api.star-history.com/svg?repos=Kosinkadink/ComfyUI-VideoHelperSuite,ComfyWorkflows/ComfyUI-Launcher,ZHO-ZHO-ZHO/ComfyUI-ZHO-Chinese,kijai/ComfyUI-Marigold,kijai/ComfyUI-IC-Light&type=Date"><img src="https://api.star-history.com/svg?repos=Kosinkadink/ComfyUI-VideoHelperSuite,ComfyWorkflows/ComfyUI-Launcher,ZHO-ZHO-ZHO/ComfyUI-ZHO-Chinese,kijai/ComfyUI-Marigold,kijai/ComfyUI-IC-Light&type=Date" alt="Star History Chart" width="500"></a></details>


## 76. Kosinkadink/ComfyUI-VideoHelperSuite


<a href='https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite'>
<img src="https://avatars.githubusercontent.com/u/7365912?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite

**Stars**: `378` | **Created at**: `2023-09-23` | **Last updated**: `2024-06-07` | **Tags**: `Custom Nodes` `Video`


Nodes related to video workflows
<details><summary>Included Nodes (29)</summary>

 - <sub>VHS_BatchManager</sub>, <sub>VHS_DuplicateImages</sub>, <sub>VHS_DuplicateLatents</sub>, <sub>VHS_DuplicateMasks</sub>, <sub>VHS_GetImageCount</sub>, <sub>VHS_GetLatentCount</sub>, <sub>VHS_GetMaskCount</sub>, <sub>VHS_LoadAudio</sub>, <sub>VHS_LoadAudioUpload</sub>, <sub>VHS_LoadImages</sub>, <sub>VHS_LoadImagesPath</sub>, <sub>VHS_LoadVideo</sub>, <sub>VHS_LoadVideoPath</sub>, <sub>VHS_MergeImages</sub>, <sub>VHS_MergeLatents</sub>, <sub>VHS_MergeMasks</sub>, <sub>VHS_PruneOutputs</sub>, <sub>VHS_SelectEveryNthImage</sub>, <sub>VHS_SelectEveryNthLatent</sub>, <sub>VHS_SelectEveryNthMask</sub>, <sub>VHS_SplitImages</sub>, <sub>VHS_SplitLatents</sub>, <sub>VHS_SplitMasks</sub>, <sub>VHS_VAEDecodeBatched</sub>, <sub>VHS_VAEEncodeBatched</sub>, <sub>VHS_VideoCombine</sub>, <sub>VHS_VideoInfo</sub>, <sub>VHS_VideoInfoLoaded</sub>, <sub>VHS_VideoInfoSource</sub>
</details>


## 77. ComfyWorkflows/ComfyUI-Launcher


<a href='https://github.com/ComfyWorkflows/ComfyUI-Launcher'>
<img src="https://avatars.githubusercontent.com/u/159965932?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/ComfyWorkflows/ComfyUI-Launcher

**Stars**: `374` | **Created at**: `2024-02-19` | **Last updated**: `2024-06-08` | **Tags**: `Management`


Run any ComfyUI workflow w/ ZERO setup.

## 78. ZHO-ZHO-ZHO/ComfyUI-ZHO-Chinese


<a href='https://github.com/ZHO-ZHO-ZHO/ComfyUI-ZHO-Chinese'>
<img src="https://avatars.githubusercontent.com/u/140084057?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/ZHO-ZHO-ZHO/ComfyUI-ZHO-Chinese

**Stars**: `374` | **Created at**: `2023-08-03` | **Last updated**: `2024-06-06` | **Tags**: `Translation` `Chinese Language`


简体中文版 ComfyUI

## 79. kijai/ComfyUI-Marigold


<a href='https://github.com/kijai/ComfyUI-Marigold'>
<img src="https://avatars.githubusercontent.com/u/40791699?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/kijai/ComfyUI-Marigold

**Stars**: `368` | **Created at**: `2023-12-12` | **Last updated**: `2024-06-09` | **Tags**: `Custom Nodes`


Marigold depth estimation in ComfyUI
<details><summary>Included Nodes (8)</summary>

 - <sub>ColorizeDepthmap</sub>
 - <sub>MarigoldDepthEstimation</sub>, <sub>MarigoldDepthEstimation_v2</sub>, <sub>MarigoldDepthEstimation_v2_video</sub>, <sub>MarigoldDepthEstimationVideo</sub>, <sub>MarigoldModelLoader</sub>
 - <sub>RemapDepth</sub>
 - <sub>SaveImageOpenEXR</sub>
</details>


## 80. kijai/ComfyUI-IC-Light


<a href='https://github.com/kijai/ComfyUI-IC-Light'>
<img src="https://avatars.githubusercontent.com/u/40791699?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/kijai/ComfyUI-IC-Light

**Stars**: `359` | **Created at**: `2024-05-09` | **Last updated**: `2024-06-09` | **Tags**: `Custom Nodes`


Using IC-LIght models in ComfyUI
<details><summary>Included Nodes (7)</summary>

 - <sub>BackgroundScaler</sub>
 - <sub>CalculateNormalsFromImages</sub>
 - <sub>DetailTransfer</sub>
 - <sub>ICLightConditioning</sub>
 - <sub>LightSource</sub>, <sub>LoadAndApplyICLightUnet</sub>, <sub>LoadHDRImage</sub>
</details>

# TOP 81 - 85

<details><summary>Star History for TOP 81 - 85</summary><a href="https://api.star-history.com/svg?repos=huchenlei/ComfyUI-IC-Light-Native,lks-ai/anynode,chaojie/ComfyUI-DragNUWA,Nuked88/ComfyUI-N-Sidebar,flowtyone/ComfyUI-Flowty-TripoSR&type=Date"><img src="https://api.star-history.com/svg?repos=huchenlei/ComfyUI-IC-Light-Native,lks-ai/anynode,chaojie/ComfyUI-DragNUWA,Nuked88/ComfyUI-N-Sidebar,flowtyone/ComfyUI-Flowty-TripoSR&type=Date" alt="Star History Chart" width="500"></a></details>


## 81. huchenlei/ComfyUI-IC-Light-Native


<a href='https://github.com/huchenlei/ComfyUI-IC-Light-Native'>
<img src="https://avatars.githubusercontent.com/u/20929282?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/huchenlei/ComfyUI-IC-Light-Native

**Stars**: `359` | **Created at**: `2024-05-08` | **Last updated**: `2024-06-09` | **Tags**: `Custom Nodes`


ComfyUI native implementation of IC-Light
<details><summary>Included Nodes (3)</summary>

 - <sub>ICLightApplyMaskGrey</sub>, <sub>ICLightAppply</sub>
 - <sub>VAEEncodeArgMax</sub>
</details>


## 82. lks-ai/anynode


<a href='https://github.com/lks-ai/anynode'>
<img src="https://avatars.githubusercontent.com/u/163685473?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/lks-ai/anynode

**Stars**: `357` | **Created at**: `2024-05-25` | **Last updated**: `2024-06-09` | **Tags**: `Custom Nodes` `LLM`


A Node for ComfyUI that does what you ask it to do
<details><summary>Included Nodes (5)</summary>

 - <sub>AnyNode</sub>, <sub>AnyNodeCodeViewer</sub>, <sub>AnyNodeExport</sub>, <sub>AnyNodeGemini</sub>, <sub>AnyNodeLocal</sub>
</details>


## 83. chaojie/ComfyUI-DragNUWA


<a href='https://github.com/chaojie/ComfyUI-DragNUWA'>
<img src="https://avatars.githubusercontent.com/u/701810?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/chaojie/ComfyUI-DragNUWA

**Stars**: `355` | **Created at**: `2024-01-11` | **Last updated**: `2024-06-07` | **Tags**: `Custom Nodes`


None
<details><summary>Included Nodes (20)</summary>

 - <sub>BrushMotion</sub>
 - <sub>CompositeMotionBrush</sub>, <sub>CompositeMotionBrushWithoutModel</sub>
 - <sub>DragNUWA Run</sub>, <sub>DragNUWA Run MotionBrush</sub>
 - <sub>Get First Image</sub>, <sub>Get Last Image</sub>
 - <sub>InstantCameraMotionBrush</sub>, <sub>InstantObjectMotionBrush</sub>
 - <sub>Load CheckPoint DragNUWA</sub>, <sub>Load MotionBrush From Optical Flow</sub>, <sub>Load MotionBrush From Optical Flow Directory</sub>, <sub>Load MotionBrush From Optical Flow Without Model</sub>, <sub>Load MotionBrush From Tracking Points</sub>, <sub>Load MotionBrush From Tracking Points Without Model</sub>, <sub>Load Pose KeyPoints</sub>, <sub>Loop</sub>, <sub>LoopEnd_IMAGE</sub>, <sub>LoopStart_IMAGE</sub>
 - <sub>Split Tracking Points</sub>
</details>


## 84. Nuked88/ComfyUI-N-Sidebar


<a href='https://github.com/Nuked88/ComfyUI-N-Sidebar'>
<img src="https://avatars.githubusercontent.com/u/1554140?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/Nuked88/ComfyUI-N-Sidebar

**Stars**: `349` | **Created at**: `2024-03-20` | **Last updated**: `2024-06-09` | **Tags**: `Management`


A simple sidebar for your ConfyUI!

## 85. flowtyone/ComfyUI-Flowty-TripoSR


<a href='https://github.com/flowtyone/ComfyUI-Flowty-TripoSR'>
<img src="https://avatars.githubusercontent.com/u/145925146?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/flowtyone/ComfyUI-Flowty-TripoSR

**Stars**: `347` | **Created at**: `2024-03-05` | **Last updated**: `2024-06-03` | **Tags**: `Custom Nodes`


TripoSR custom node for comfyui
<details><summary>Included Nodes (3)</summary>

 - <sub>TripoSRModelLoader</sub>, <sub>TripoSRSampler</sub>, <sub>TripoSRViewer</sub>
</details>

# TOP 86 - 90

<details><summary>Star History for TOP 86 - 90</summary><a href="https://api.star-history.com/svg?repos=ai-dock/comfyui,BlenderNeko/ComfyUI_Cutoff,AuroBit/ComfyUI-OOTDiffusion,melMass/comfy_mtb,Fannovel16/ComfyUI-Frame-Interpolation&type=Date"><img src="https://api.star-history.com/svg?repos=ai-dock/comfyui,BlenderNeko/ComfyUI_Cutoff,AuroBit/ComfyUI-OOTDiffusion,melMass/comfy_mtb,Fannovel16/ComfyUI-Frame-Interpolation&type=Date" alt="Star History Chart" width="500"></a></details>


## 86. ai-dock/comfyui


<a href='https://github.com/ai-dock/comfyui'>
<img src="https://avatars.githubusercontent.com/u/138283508?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/ai-dock/comfyui

**Stars**: `345` | **Created at**: `2023-08-22` | **Last updated**: `2024-06-08` | **Tags**: `Integration`


ComfyUI docker images for use in GPU cloud and local environments. Includes AI-Dock base for authentication and improved user experience. 

## 87. BlenderNeko/ComfyUI_Cutoff


<a href='https://github.com/BlenderNeko/ComfyUI_Cutoff'>
<img src="https://avatars.githubusercontent.com/u/126974546?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/BlenderNeko/ComfyUI_Cutoff

**Stars**: `328` | **Created at**: `2023-04-02` | **Last updated**: `2024-06-09` | **Tags**: `Custom Nodes`


cutoff implementation for ComfyUI
<details><summary>Included Nodes (4)</summary>

 - <sub>BNK_CutoffBasePrompt</sub>, <sub>BNK_CutoffRegionsToConditioning</sub>, <sub>BNK_CutoffRegionsToConditioning_ADV</sub>, <sub>BNK_CutoffSetRegions</sub>
</details>


## 88. AuroBit/ComfyUI-OOTDiffusion


<a href='https://github.com/AuroBit/ComfyUI-OOTDiffusion'>
<img src="https://avatars.githubusercontent.com/u/135130495?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/AuroBit/ComfyUI-OOTDiffusion

**Stars**: `326` | **Created at**: `2024-02-23` | **Last updated**: `2024-06-07` | **Tags**: `Custom Nodes` `Chinese Language`


ComfyUI custom node that simply integrates the OOTDiffusion.

## 89. melMass/comfy_mtb


<a href='https://github.com/melMass/comfy_mtb'>
<img src="https://avatars.githubusercontent.com/u/7041726?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/melMass/comfy_mtb

**Stars**: `326` | **Created at**: `2023-06-03` | **Last updated**: `2024-06-07` | **Tags**: `Custom Nodes` `Video`


Animation oriented nodes pack for ComfyUI
<details><summary>Included Nodes (60)</summary>

 - <sub>Animation Builder (mtb)</sub>, <sub>Any To String (mtb)</sub>
 - <sub>Batch Float (mtb)</sub>, <sub>Batch Float Assemble (mtb)</sub>, <sub>Batch Float Fill (mtb)</sub>, <sub>Batch Make (mtb)</sub>, <sub>Batch Merge (mtb)</sub>, <sub>Batch Shake (mtb)</sub>, <sub>Batch Shape (mtb)</sub>, <sub>Batch Transform (mtb)</sub>, <sub>Bbox (mtb)</sub>, <sub>Bbox From Mask (mtb)</sub>, <sub>Blur (mtb)</sub>
 - <sub>Color Correct (mtb)</sub>, <sub>Colored Image (mtb)</sub>, <sub>Concat Images (mtb)</sub>, <sub>Crop (mtb)</sub>
 - <sub>Debug (mtb)</sub>, <sub>Deep Bump (mtb)</sub>
 - <sub>Export With Ffmpeg (mtb)</sub>
 - <sub>Face Swap (mtb)</sub>, <sub>Film Interpolation (mtb)</sub>, <sub>Fit Number (mtb)</sub>, <sub>Float To Number (mtb)</sub>
 - <sub>Get Batch From History (mtb)</sub>
 - <sub>Image Compare (mtb)</sub>, <sub>Image Premultiply (mtb)</sub>, <sub>Image Remove Background Rembg (mtb)</sub>, <sub>Image Resize Factor (mtb)</sub>, <sub>Image Tile Offset (mtb)</sub>, <sub>Int To Bool (mtb)</sub>, <sub>Int To Number (mtb)</sub>, <sub>Interpolate Clip Sequential (mtb)</sub>
 - <sub>Latent Lerp (mtb)</sub>, <sub>Load Face Analysis Model (mtb)</sub>, <sub>Load Face Enhance Model (mtb)</sub>, <sub>Load Face Swap Model (mtb)</sub>, <sub>Load Film Model (mtb)</sub>, <sub>Load Image From Url (mtb)</sub>, <sub>Load Image Sequence (mtb)</sub>
 - <sub>Mask To Image (mtb)</sub>, <sub>Math Expression (mtb)</sub>, <sub>Model Patch Seamless (mtb)</sub>
 - <sub>Pick From Batch (mtb)</sub>
 - <sub>Qr Code (mtb)</sub>
 - <sub>Restore Face (mtb)</sub>
 - <sub>Save Gif (mtb)</sub>, <sub>Save Image Grid (mtb)</sub>, <sub>Save Image Sequence (mtb)</sub>, <sub>Save Tensors (mtb)</sub>, <sub>Sharpen (mtb)</sub>, <sub>Smart Step (mtb)</sub>, <sub>Stack Images (mtb)</sub>, <sub>String Replace (mtb)</sub>, <sub>Styles Loader (mtb)</sub>
 - <sub>Text To Image (mtb)</sub>, <sub>Transform Image (mtb)</sub>
 - <sub>Uncrop (mtb)</sub>, <sub>Unsplash Image (mtb)</sub>
 - <sub>Vae Decode (mtb)</sub>
</details>


## 90. Fannovel16/ComfyUI-Frame-Interpolation


<a href='https://github.com/Fannovel16/ComfyUI-Frame-Interpolation'>
<img src="https://avatars.githubusercontent.com/u/16047777?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/Fannovel16/ComfyUI-Frame-Interpolation

**Stars**: `326` | **Created at**: `2023-07-31` | **Last updated**: `2024-06-08` | **Tags**: `Custom Nodes` `Video`


A custom node set for Video Frame Interpolation in ComfyUI.
<details><summary>Included Nodes (14)</summary>

 - <sub>AMT VFI</sub>
 - <sub>CAIN VFI</sub>
 - <sub>FILM VFI</sub>, <sub>FLAVR VFI</sub>
 - <sub>GMFSS Fortuna VFI</sub>
 - <sub>IFRNet VFI</sub>, <sub>IFUnet VFI</sub>
 - <sub>KSampler Gradually Adding More Denoise (efficient)</sub>
 - <sub>M2M VFI</sub>, <sub>Make Interpolation State List</sub>
 - <sub>RIFE VFI</sub>
 - <sub>Sepconv VFI</sub>, <sub>STMFNet VFI</sub>
 - <sub>VFI FloatToInt</sub>
</details>

# TOP 91 - 95

<details><summary>Star History for TOP 91 - 95</summary><a href="https://api.star-history.com/svg?repos=xXAdonesXx/NodeGPT,ZHO-ZHO-ZHO/ComfyUI-ArtGallery,if-ai/ComfyUI-IF_AI_tools,atlasunified/Templates-ComfyUI-,nullquant/ComfyUI-BrushNet&type=Date"><img src="https://api.star-history.com/svg?repos=xXAdonesXx/NodeGPT,ZHO-ZHO-ZHO/ComfyUI-ArtGallery,if-ai/ComfyUI-IF_AI_tools,atlasunified/Templates-ComfyUI-,nullquant/ComfyUI-BrushNet&type=Date" alt="Star History Chart" width="500"></a></details>


## 91. xXAdonesXx/NodeGPT


<a href='https://github.com/xXAdonesXx/NodeGPT'>
<img src="https://avatars.githubusercontent.com/u/66518617?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/xXAdonesXx/NodeGPT

**Stars**: `322` | **Created at**: `2023-04-08` | **Last updated**: `2024-06-07` | **Tags**: `Custom Nodes` `LLM`


ComfyUI Extension Nodes for Automated Text Generation.
<details><summary>Included Nodes (36)</summary>

 - <sub>AppendAgent</sub>, <sub>Assistant</sub>
 - <sub>Chat</sub>, <sub>ChatGPT</sub>, <sub>CombineInput</sub>, <sub>Conditioning</sub>, <sub>CostumeAgent_1</sub>, <sub>CostumeAgent_2</sub>, <sub>CostumeMaster_1</sub>, <sub>Critic</sub>
 - <sub>DisplayString</sub>, <sub>DisplayTextAsImage</sub>
 - <sub>Engineer</sub>, <sub>EVAL</sub>, <sub>Executor</sub>
 - <sub>GroupChat</sub>
 - <sub>Image_generation_Conditioning</sub>
 - <sub>llama-cpp</sub>, <sub>llava</sub>, <sub>LM_Studio</sub>, <sub>LoadAPIconfig</sub>, <sub>LoadTXT</sub>
 - <sub>MemGPT</sub>, <sub>Memory_Excel</sub>, <sub>Model_1</sub>
 - <sub>Ollama</sub>, <sub>oobaboogaOpenAI</sub>, <sub>Output2String</sub>
 - <sub>Planner</sub>
 - <sub>Scientist</sub>
 - <sub>TextCombine</sub>, <sub>TextGeneration</sub>, <sub>TextGenerator</sub>, <sub>TextInput</sub>, <sub>TextOutput</sub>
 - <sub>UserProxy</sub>
</details>


## 92. ZHO-ZHO-ZHO/ComfyUI-ArtGallery


<a href='https://github.com/ZHO-ZHO-ZHO/ComfyUI-ArtGallery'>
<img src="https://avatars.githubusercontent.com/u/140084057?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/ZHO-ZHO-ZHO/ComfyUI-ArtGallery

**Stars**: `321` | **Created at**: `2023-12-27` | **Last updated**: `2024-06-08` | **Tags**: `Custom Nodes` `Chinese Language`


Prompt Visualization | Art Gallery
<details><summary>Included Nodes (6)</summary>

 - <sub>ArtGallery_Zho</sub>, <sub>ArtistsImage_Zho</sub>
 - <sub>CamerasImage_Zho</sub>
 - <sub>FilmsImage_Zho</sub>
 - <sub>MovementsImage_Zho</sub>
 - <sub>StylesImage_Zho</sub>
</details>


## 93. if-ai/ComfyUI-IF_AI_tools


<a href='https://github.com/if-ai/ComfyUI-IF_AI_tools'>
<img src="https://avatars.githubusercontent.com/u/21185218?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/if-ai/ComfyUI-IF_AI_tools

**Stars**: `319` | **Created at**: `2024-03-12` | **Last updated**: `2024-06-08` | **Tags**: `Custom Nodes` `LLM`


ComfyUI-IF_AI_tools is a set of custom nodes for ComfyUI that allows you to generate prompts using a local Large Language Model (LLM) via Ollama. This tool enables you to enhance your image generation workflow by leveraging the power of language models.
<details><summary>Included Nodes (6)</summary>

 - <sub>IF_ChatPrompt</sub>, <sub>IF_DisplayText</sub>, <sub>IF_ImagePrompt</sub>, <sub>IF_PromptMkr</sub>, <sub>IF_SaveText</sub>, <sub>IF_saveText</sub>
</details>


## 94. atlasunified/Templates-ComfyUI-


<a href='https://github.com/atlasunified/Templates-ComfyUI-'>
<img src="https://avatars.githubusercontent.com/u/113645143?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/atlasunified/Templates-ComfyUI-

**Stars**: `317` | **Created at**: `2023-02-27` | **Last updated**: `2024-06-09` | **Tags**: `Workflow Examples`


Templates to view the variety of a prompt based on the samplers available in ComfyUI. Variety of sizes and singlular seed and random seed templates.

## 95. nullquant/ComfyUI-BrushNet


<a href='https://github.com/nullquant/ComfyUI-BrushNet'>
<img src="https://avatars.githubusercontent.com/u/81931994?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/nullquant/ComfyUI-BrushNet

**Stars**: `315` | **Created at**: `2024-04-11` | **Last updated**: `2024-06-09` | **Tags**: `Custom Nodes`


ComfyUI BrushNet nodes
<details><summary>Included Nodes (8)</summary>

 - <sub>BlendInpaint</sub>, <sub>BrushNet</sub>, <sub>BrushNetLoader</sub>
 - <sub>CutForInpaint</sub>
 - <sub>PowerPaint</sub>, <sub>PowerPaintCLIPLoader</sub>
 - <sub>RAUNet</sub>
 - <sub>Terminal</sub>
</details>

# TOP 96 - 100

<details><summary>Star History for TOP 96 - 100</summary><a href="https://api.star-history.com/svg?repos=kijai/ComfyUI-IC-Light-Wrapper,ZHO-ZHO-ZHO/ComfyUI-APISR,kijai/ComfyUI-KJNodes,kijai/ComfyUI-DiffusersStableCascade,TinyTerra/ComfyUI_tinyterraNodes&type=Date"><img src="https://api.star-history.com/svg?repos=kijai/ComfyUI-IC-Light-Wrapper,ZHO-ZHO-ZHO/ComfyUI-APISR,kijai/ComfyUI-KJNodes,kijai/ComfyUI-DiffusersStableCascade,TinyTerra/ComfyUI_tinyterraNodes&type=Date" alt="Star History Chart" width="500"></a></details>


## 96. kijai/ComfyUI-IC-Light-Wrapper


<a href='https://github.com/kijai/ComfyUI-IC-Light-Wrapper'>
<img src="https://avatars.githubusercontent.com/u/40791699?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/kijai/ComfyUI-IC-Light-Wrapper

**Stars**: `313` | **Created at**: `2024-05-08` | **Last updated**: `2024-06-02` | **Tags**: `Custom Nodes`


Wraps the IC-Light Diffuser demo to a ComfyUI node

## 97. ZHO-ZHO-ZHO/ComfyUI-APISR


<a href='https://github.com/ZHO-ZHO-ZHO/ComfyUI-APISR'>
<img src="https://avatars.githubusercontent.com/u/140084057?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/ZHO-ZHO-ZHO/ComfyUI-APISR

**Stars**: `310` | **Created at**: `2024-03-19` | **Last updated**: `2024-06-06` | **Tags**: `Custom Nodes` `Chinese Language`


Unofficial implementation of APISR for ComfyUI
<details><summary>Included Nodes (3)</summary>

 - <sub>APISR_Lterative_Zho</sub>, <sub>APISR_ModelLoader_Zho</sub>, <sub>APISR_Zho</sub>
</details>


## 98. kijai/ComfyUI-KJNodes


<a href='https://github.com/kijai/ComfyUI-KJNodes'>
<img src="https://avatars.githubusercontent.com/u/40791699?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/kijai/ComfyUI-KJNodes

**Stars**: `308` | **Created at**: `2023-09-28` | **Last updated**: `2024-06-08` | **Tags**: `Custom Nodes`


Various custom nodes for ComfyUI
<details><summary>Included Nodes (112)</summary>

 - <sub>AddLabel</sub>, <sub>AppendInstanceDiffusionTracking</sub>
 - <sub>BatchCLIPSeg</sub>, <sub>BatchCropFromMask</sub>, <sub>BatchCropFromMaskAdvanced</sub>, <sub>BatchUncrop</sub>, <sub>BatchUncropAdvanced</sub>, <sub>BboxToInt</sub>, <sub>BboxVisualize</sub>
 - <sub>CameraPoseVisualizer</sub>, <sub>ColorMatch</sub>, <sub>ColorToMask</sub>, <sub>ConditioningMultiCombine</sub>, <sub>ConditioningSetMaskAndCombine</sub>, <sub>ConditioningSetMaskAndCombine3</sub>, <sub>ConditioningSetMaskAndCombine4</sub>, <sub>ConditioningSetMaskAndCombine5</sub>, <sub>CondPassThrough</sub>, <sub>CreateAudioMask</sub>, <sub>CreateFadeMask</sub>, <sub>CreateFadeMaskAdvanced</sub>, <sub>CreateFluidMask</sub>, <sub>CreateGradientFromCoords</sub>, <sub>CreateGradientMask</sub>, <sub>CreateInstanceDiffusionTracking</sub>, <sub>CreateMagicMask</sub>, <sub>CreateShapeImageOnPath</sub>, <sub>CreateShapeMask</sub>, <sub>CreateShapeMaskOnPath</sub>, <sub>CreateTextMask</sub>, <sub>CreateTextOnPath</sub>, <sub>CreateVoronoiMask</sub>, <sub>CrossFadeImages</sub>, <sub>CustomSigmas</sub>
 - <sub>DownloadAndLoadCLIPSeg</sub>, <sub>DrawInstanceDiffusionTracking</sub>, <sub>DummyLatentOut</sub>
 - <sub>EmptyLatentImagePresets</sub>
 - <sub>FilterZeroMasksAndCorrespondingImages</sub>, <sub>FlipSigmasAdjusted</sub>, <sub>FloatConstant</sub>, <sub>FloatToMask</sub>, <sub>FloatToSigmas</sub>
 - <sub>GenerateNoise</sub>, <sub>GetImageRangeFromBatch</sub>, <sub>GetImagesFromBatchIndexed</sub>, <sub>GetImageSizeAndCount</sub>, <sub>GetLatentsFromBatchIndexed</sub>, <sub>GetMaskSizeAndCount</sub>, <sub>GLIGENTextBoxApplyBatchCoords</sub>, <sub>GradientToFloat</sub>, <sub>GrowMaskWithBlur</sub>
 - <sub>ImageAddMulti</sub>, <sub>ImageAndMaskPreview</sub>, <sub>ImageBatchMulti</sub>, <sub>ImageBatchRepeatInterleaving</sub>, <sub>ImageBatchTestPattern</sub>, <sub>ImageConcanate</sub>, <sub>ImageGrabPIL</sub>, <sub>ImageGridComposite2x2</sub>, <sub>ImageGridComposite3x3</sub>, <sub>ImageNormalize_Neg1_To_1</sub>, <sub>ImagePadForOutpaintMasked</sub>, <sub>ImagePadForOutpaintTargetSize</sub>, <sub>ImagePass</sub>, <sub>ImageResizeKJ</sub>, <sub>ImageTransformByNormalizedAmplitude</sub>, <sub>ImageUpscaleWithModelBatched</sub>, <sub>InjectNoiseToLatent</sub>, <sub>InsertImageBatchByIndexes</sub>, <sub>InsertImagesToBatchIndexed</sub>, <sub>INTConstant</sub>, <sub>InterpolateCoords</sub>, <sub>Intrinsic_lora_sampling</sub>
 - <sub>JoinStringMulti</sub>, <sub>JoinStrings</sub>
 - <sub>LoadAndResizeImage</sub>, <sub>LoadResAdapterNormalization</sub>
 - <sub>MaskBatchMulti</sub>, <sub>MaskOrImageToWeight</sub>, <sub>MergeImageChannels</sub>, <sub>ModelPassThrough</sub>
 - <sub>NormalizedAmplitudeToFloatList</sub>, <sub>NormalizedAmplitudeToMask</sub>
 - <sub>OffsetMask</sub>, <sub>OffsetMaskByNormalizedAmplitude</sub>
 - <sub>PlotCoordinates</sub>, <sub>PreviewAnimation</sub>
 - <sub>RemapImageRange</sub>, <sub>RemapMaskRange</sub>, <sub>ReplaceImagesInBatch</sub>, <sub>ResizeMask</sub>, <sub>ReverseImageBatch</sub>, <sub>RoundMask</sub>
 - <sub>SaveImageWithAlpha</sub>, <sub>ScaleBatchPromptSchedule</sub>, <sub>Sleep</sub>, <sub>SomethingToString</sub>, <sub>SoundReactive</sub>, <sub>SplineEditor</sub>, <sub>SplitBboxes</sub>, <sub>SplitImageChannels</sub>, <sub>StabilityAPI_SD3</sub>, <sub>StableZero123_BatchSchedule</sub>, <sub>StringConstant</sub>, <sub>StringConstantMultiline</sub>, <sub>Superprompt</sub>, <sub>SV3D_BatchSchedule</sub>
 - <sub>VRAM_Debug</sub>
 - <sub>WeightScheduleConvert</sub>, <sub>WeightScheduleExtend</sub>, <sub>WidgetToString</sub>
</details>


## 99. kijai/ComfyUI-DiffusersStableCascade


<a href='https://github.com/kijai/ComfyUI-DiffusersStableCascade'>
<img src="https://avatars.githubusercontent.com/u/40791699?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/kijai/ComfyUI-DiffusersStableCascade

**Stars**: `307` | **Created at**: `2024-02-13` | **Last updated**: `2024-06-05` | **Tags**: `Deprecated`


Simple inference with StableCascade using diffusers in ComfyUI

## 100. TinyTerra/ComfyUI_tinyterraNodes


<a href='https://github.com/TinyTerra/ComfyUI_tinyterraNodes'>
<img src="https://avatars.githubusercontent.com/u/115619949?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/TinyTerra/ComfyUI_tinyterraNodes

**Stars**: `307` | **Created at**: `2023-05-11` | **Last updated**: `2024-06-07` | **Tags**: `Custom Nodes`


A selection of nodes for Stable Diffusion ComfyUI
<details><summary>Included Nodes (38)</summary>

 - <sub>ttN advanced xyPlot</sub>, <sub>ttN advPlot range</sub>, <sub>ttN compareInput</sub>, <sub>ttN concat</sub>, <sub>ttN conditioning</sub>, <sub>ttN debugInput</sub>, <sub>ttN float</sub>, <sub>ttN hiresfixScale</sub>, <sub>ttN imageOutput</sub>, <sub>ttN imageREMBG</sub>, <sub>ttN int</sub>, <sub>ttN KSampler_v2</sub>, <sub>ttN multiModelMerge</sub>, <sub>ttN pipe2BASIC</sub>, <sub>ttN pipe2DETAILER</sub>, <sub>ttN pipeEDIT</sub>, <sub>ttN pipeEncodeConcat</sub>, <sub>ttN pipeIN</sub>, <sub>ttN pipeKSampler</sub>, <sub>ttN pipeKSampler_v2</sub>, <sub>ttN pipeKSamplerAdvanced</sub>, <sub>ttN pipeKSamplerAdvanced_v2</sub>, <sub>ttN pipeKSamplerSDXL</sub>, <sub>ttN pipeKSamplerSDXL_v2</sub>, <sub>ttN pipeLoader</sub>, <sub>ttN pipeLoader_v2</sub>, <sub>ttN pipeLoaderSDXL</sub>, <sub>ttN pipeLoaderSDXL_v2</sub>, <sub>ttN pipeLoraStack</sub>, <sub>ttN pipeOUT</sub>, <sub>ttN seed</sub>, <sub>ttN text</sub>, <sub>ttN text3BOX_3WAYconcat</sub>, <sub>ttN text7BOX_concat</sub>, <sub>ttN textCycleLine</sub>, <sub>ttN textDebug</sub>, <sub>ttN tinyLoader</sub>, <sub>ttN xyPlot</sub>
</details>


## By Date

You can also view this list in the order of creation date (to get a sense of the history of ComfyUI) [here](byDate.md).

## A Broader Collection

There are also many repositories refer to `ComfyUI` in their `README.md`.
This broader collection can be found [here](BroaderCollection.md).

## Data Source

This list is based on data from the `GitHub Search API`, `Star History API`, `ComfyUI-Manager`, and `manually curated tags`.
 * The GitHub Search API is used to find repositories based on the query `comfyui fork:true`, sorted by the number of stars.
 * The Star History API provides the star count history for these repositories.
 * ComfyUI-Manager provides the node list via the [extension_node_map](https://raw.githubusercontent.com/ltdrdata/ComfyUI-Manager/main/extension-node-map.json).
 * Manual tags are used to categorize and filter repositories.

Code can be found in [main.py](main.py). Manual tags are stored in [tags.yml](tags.yml).

All rights belong to the original authors of the repositories.

### Automatically updated on: 2024-06-09 08:45:14 UTC
