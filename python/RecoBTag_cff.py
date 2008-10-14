import FWCore.ParameterSet.Config as cms

# define the b-tag squences for offline reconstruction
from RecoBTag.SoftLepton.softLepton_cff import *
from RecoBTag.ImpactParameter.impactParameter_cff import *
from RecoBTag.SecondaryVertex.secondaryVertex_cff import *

btagging = cms.Sequence(
    impactParameterTagInfos * 
    jetBProbabilityBJetTags + 
    jetProbabilityBJetTags + 
    trackCountingHighPurBJetTags + 
    trackCountingHighEffBJetTags + 
    impactParameterMVABJetTags * 
    secondaryVertexTagInfos * 
    simpleSecondaryVertexBJetTags + 
    combinedSecondaryVertexBJetTags + 
    combinedSecondaryVertexMVABJetTags + 
    btagSoftElectrons * 
    softElectronTagInfos * 
    softElectronBJetTags + 
    softMuonTagInfos * 
    softMuonBJetTags + 
    softMuonNoIPBJetTags +
    softLeptonByPtBJetTags
)
