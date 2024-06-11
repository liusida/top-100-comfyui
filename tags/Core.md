# Repositories tagged with `Core`


## comfyanonymous/ComfyUI


<a href='https://github.com/comfyanonymous/ComfyUI'>
<img src="https://avatars.githubusercontent.com/u/121283862?v=4" width="50" height="50"></a> &nbsp; &nbsp; https://github.com/comfyanonymous/ComfyUI

**Stars**: `37.2k` | **Created at**: `2024-06-10`


The most powerful and modular stable diffusion GUI, api and backend with a graph/nodes interface.
<details><summary>Included Nodes (179)</summary>

 - <sub>AddNoise</sub>, <sub>[AlignYourStepsScheduler](node_examples/AlignYourStepsScheduler.md)</sub>
 - <sub>BasicGuider</sub>, <sub>[BasicScheduler](node_examples/BasicScheduler.md)</sub>
 - <sub>[Canny](node_examples/Canny.md)</sub>, <sub>[CFGGuider](node_examples/CFGGuider.md)</sub>, <sub>CheckpointLoader</sub>, [CheckpointLoaderSimple🌟](node_examples/CheckpointLoaderSimple.md), <sub>[CheckpointSave](node_examples/CheckpointSave.md)</sub>, <sub>CLIPAttentionMultiply</sub>, <sub>[CLIPLoader](node_examples/CLIPLoader.md)</sub>, <sub>CLIPMergeAdd</sub>, <sub>[CLIPMergeSimple](node_examples/CLIPMergeSimple.md)</sub>, <sub>CLIPMergeSubtract</sub>, <sub>CLIPSave</sub>, [CLIPSetLastLayer🌟](node_examples/CLIPSetLastLayer.md), [CLIPTextEncode🌟](node_examples/CLIPTextEncode.md), <sub>CLIPTextEncodeControlnet</sub>, [CLIPTextEncodeSDXL🌟](node_examples/CLIPTextEncodeSDXL.md), [CLIPTextEncodeSDXLRefiner🌟](node_examples/CLIPTextEncodeSDXLRefiner.md), [CLIPVisionEncode🌟](node_examples/CLIPVisionEncode.md), [CLIPVisionLoader🌟](node_examples/CLIPVisionLoader.md), <sub>[ConditioningAverage](node_examples/ConditioningAverage.md)</sub>, [ConditioningCombine🌟](node_examples/ConditioningCombine.md), <sub>[ConditioningConcat](node_examples/ConditioningConcat.md)</sub>, <sub>[ConditioningSetArea](node_examples/ConditioningSetArea.md)</sub>, <sub>ConditioningSetAreaPercentage</sub>, <sub>ConditioningSetAreaStrength</sub>, <sub>[ConditioningSetMask](node_examples/ConditioningSetMask.md)</sub>, <sub>[ConditioningSetTimestepRange](node_examples/ConditioningSetTimestepRange.md)</sub>, <sub>[ConditioningZeroOut](node_examples/ConditioningZeroOut.md)</sub>, <sub>[ControlNetApply](node_examples/ControlNetApply.md)</sub>, [ControlNetApplyAdvanced🌟](node_examples/ControlNetApplyAdvanced.md), [ControlNetLoader🌟](node_examples/ControlNetLoader.md), <sub>CropMask</sub>
 - <sub>[DiffControlNetLoader](node_examples/DiffControlNetLoader.md)</sub>, <sub>[DifferentialDiffusion](node_examples/DifferentialDiffusion.md)</sub>, <sub>[DiffusersLoader](node_examples/DiffusersLoader.md)</sub>, <sub>DisableNoise</sub>, <sub>[DualCFGGuider](node_examples/DualCFGGuider.md)</sub>, <sub>[DualCLIPLoader](node_examples/DualCLIPLoader.md)</sub>
 - <sub>[EmptyImage](node_examples/EmptyImage.md)</sub>, [EmptyLatentImage🌟](node_examples/EmptyLatentImage.md), <sub>ExponentialScheduler</sub>
 - <sub>[FeatherMask](node_examples/FeatherMask.md)</sub>, <sub>[FlipSigmas](node_examples/FlipSigmas.md)</sub>, <sub>[FreeU](node_examples/FreeU.md)</sub>, [FreeU_V2🌟](node_examples/FreeU_V2.md)
 - <sub>[GLIGENLoader](node_examples/GLIGENLoader.md)</sub>, <sub>[GLIGENTextBoxApply](node_examples/GLIGENTextBoxApply.md)</sub>, [GrowMask🌟](node_examples/GrowMask.md)
 - <sub>[HypernetworkLoader](node_examples/HypernetworkLoader.md)</sub>, <sub>[HyperTile](node_examples/HyperTile.md)</sub>
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

