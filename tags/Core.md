# Repositories tagged with `Core`


## comfyanonymous/ComfyUI


<a href='https://github.com/comfyanonymous/ComfyUI'>
<img src="https://avatars.githubusercontent.com/u/121283862?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/comfyanonymous/ComfyUI

**Stars**: `37.1k` | **Created at**: `2024-06-09`


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

