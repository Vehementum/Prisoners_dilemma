import axelrod
from core.match_history import match_history, score, match_history_with_noise
import inspect
import axelrod as axl
from simulation import round_robin

"""
This file imports all the strategies in to the base name space. Note that some
of the imports are imports of classes that make generic classes available to
users. In these cases the imports are done separately so that they can be
annotated as to avoid some static testing. For example:

    from .memoryone import (
        GTFT,
        ALLCorALLD,
        FirmButFair,
        SoftJoss,
        StochasticCooperator,
        StochasticWSLS,
        WinShiftLoseStay,
        WinStayLoseShift,
    )
    from .memoryone import ( # pylint: disable=unused-import
        ReactivePlayer,
        MemoryOnePlayer
    )
    # isort:skip_file
"""

import warnings

from axelrod import Adaptive
from axelrod import AdaptorBrief, AdaptorLong
from axelrod import Alternator
from axelrod import EvolvedANN, EvolvedANN5, EvolvedANNNoise05
from axelrod import ANN, EvolvableANN  # pylint: disable=unused-import
from axelrod import APavlov2006, APavlov2011
from axelrod import Appeaser
from axelrod import EvolvedAttention
from axelrod import AverageCopier, NiceAverageCopier
from axelrod import (
    FirstByDavis,
    FirstByFeld,
    FirstByGraaskamp,
    FirstByGrofman,
    FirstByJoss,
    FirstByNydegger,
    FirstByDowning,
    FirstByShubik,
    FirstBySteinAndRapoport,
    FirstByTidemanAndChieruzzi,
    FirstByTullock,
    FirstByAnonymous,
)
from axelrod import (
    SecondByAppold,
    SecondByBlack,
    SecondByBorufsen,
    SecondByCave,
    SecondByChampion,
    SecondByColbert,
    SecondByEatherley,
    SecondByGetzler,
    SecondByGladstein,
    SecondByGraaskampKatzen,
    SecondByHarrington,
    SecondByKluepfel,
    SecondByLeyvraz,
    SecondByMikkelson,
    SecondByGrofman,
    SecondByTidemanAndChieruzzi,
    SecondByRichardHufford,
    SecondByRowsam,
    SecondByTester,
    SecondByTranquilizer,
    SecondByWeiner,
    SecondByWhite,
    SecondByWmAdams,
    SecondByYamachi,
)
from axelrod import BackStabber, DoubleCrosser
from axelrod import BetterAndBetter
from axelrod import BushMosteller
from axelrod import Calculator
from axelrod import Cooperator, TrickyCooperator
from axelrod import (
    AntiCycler,
    CyclerCCCCCD,
    CyclerCCCD,
    CyclerCCCDCD,
    CyclerCCD,
    CyclerDC,
    CyclerDDC,
)
from axelrod import Cycler, EvolvableCycler  # pylint: disable=unused-import
from axelrod import Darwin
from axelrod import DBS
from axelrod import Defector, TrickyDefector
from axelrod import Doubler
from axelrod import (
    TF1,
    TF2,
    TF3,
    EvolvedFSM4,
    EvolvedFSM6,
    EvolvedFSM16,
    EvolvedFSM16Noise05,
    Fortress3,
    Fortress4,
    Predator,
    Pun1,
    Raider,
    Ripoff,
    UsuallyCooperates,
    UsuallyDefects,
    SolutionB1,
    SolutionB5,
    Thumper,
)
from axelrod import (  # pylint: disable=unused-import
    EvolvableFSMPlayer,
    FSMPlayer,
)
from axelrod import Forgiver, ForgivingTitForTat
from axelrod import (
    PSOGambler1_1_1,
    PSOGambler2_2_2,
    PSOGambler2_2_2_Noise05,
    PSOGamblerMem1,
    ZDMem2,
)
from axelrod import EvolvableGambler, Gambler  # pylint: disable=unused-import
from axelrod import (
    GoByMajority,
    GoByMajority5,
    GoByMajority10,
    GoByMajority20,
    GoByMajority40,
    HardGoByMajority,
    HardGoByMajority5,
    HardGoByMajority10,
    HardGoByMajority20,
    HardGoByMajority40,
)
from axelrod import GradualKiller
from axelrod import (
    Aggravater,
    Capri,
    EasyGo,
    ForgetfulGrudger,
    GeneralSoftGrudger,
    Grudger,
    GrudgerAlternator,
    OppositeGrudger,
    SoftGrudger,
    SpitefulCC,
)
from axelrod import Grumpy
from axelrod import Handshake
from axelrod import EvolvedHMM5
from axelrod import EvolvableHMMPlayer, HMMPlayer  # pylint: disable=unused-import

from axelrod import (
    AlternatorHunter,
    CooperatorHunter,
    CycleHunter,
    DefectorHunter,
    EventualCycleHunter,
    MathConstantHunter,
    RandomHunter,
)
from axelrod import Inverse
from axelrod import (
    EvolvedLookerUp1_1_1,
    EvolvedLookerUp2_2_2,
    Winner12,
    Winner21,
)
from axelrod import (  # pylint: disable=unused-import
    EvolvableLookerUp,
    LookerUp,
)

from axelrod import Golden, Pi, e
from axelrod import (
    GTFT,
    ALLCorALLD,
    FirmButFair,
    SoftJoss,
    StochasticCooperator,
    StochasticWSLS,
    WinShiftLoseStay,
    WinStayLoseShift,
)
from axelrod import (  # pylint: disable=unused-import
    ReactivePlayer,
    MemoryOnePlayer,
)

from axelrod import AON2, MEM2, DelayedAON1
from axelrod import MemoryTwoPlayer  # pylint: disable=unused-import

from axelrod import Momentum
from axelrod import Desperate, Hopeless, Willing
from axelrod import Negation
from axelrod import FoolMeOnce, ForgetfulFoolMeOnce, OnceBitten
from axelrod import (
    CollectiveStrategy,
    Detective,
    HardProber,
    NaiveProber,
    Prober,
    Prober2,
    Prober3,
    Prober4,
    RemorsefulProber,
)
from axelrod import (
    InversePunisher,
    LevelPunisher,
    Punisher,
    TrickyLevelPunisher,
)
from axelrod import (
    ArrogantQLearner,
    CautiousQLearner,
    HesitantQLearner,
    RiskyQLearner,
)
from axelrod import Random
from axelrod import DoubleResurrection, Resurrection
from axelrod import (
    LimitedRetaliate,
    LimitedRetaliate2,
    LimitedRetaliate3,
    Retaliate,
    Retaliate2,
    Retaliate3,
)
from axelrod import RevisedDowning
from axelrod import SelfSteem
from axelrod import (  # pylint: disable=unused-import
    SequencePlayer,
    ThueMorse,
    ThueMorseInverse,
)
from axelrod import ShortMem
from axelrod import Stalker
from axelrod import FrequencyAnalyzer
from axelrod import (
    AdaptiveTitForTat,
    Alexei,
    AntiTitForTat,
    Bully,
    BurnBothEnds,
    ContriteTitForTat,
    DynamicTwoTitsForTat,
    EugineNier,
    Gradual,
    HardTitFor2Tats,
    HardTitForTat,
    Michaelos,
    NTitsForMTats,
    OmegaTFT,
    OriginalGradual,
    RandomTitForTat,
    SlowTitForTwoTats2,
    SneakyTitForTat,
    SpitefulTitForTat,
    SuspiciousTitForTat,
    TitFor2Tats,
    TitForTat,
    TwoTitsForTat,
)
from axelrod import VeryBad
from axelrod import (
    KnowledgeableWorseAndWorse,
    WorseAndWorse,
    WorseAndWorse2,
    WorseAndWorse3,
)
from axelrod import (
    ZDGTFT2,
    ZDExtort2,
    ZDExtort2v2,
    ZDExtort3,
    ZDExtort4,
    ZDExtortion,
    ZDGen2,
    ZDMischief,
    ZDSet2,
)

# Note: Meta* strategies are handled in .__init__.py

all_strategies = [
    ALLCorALLD(),
    AON2(),
    APavlov2006(),
    APavlov2011(),
    Adaptive(),
    AdaptiveTitForTat(),
    AdaptorBrief(),
    AdaptorLong(),
    Aggravater(),
    Alexei(),
    Alternator(),
    AlternatorHunter(),
    AntiCycler(),
    AntiTitForTat(),
    Appeaser(),
    ArrogantQLearner(),
    AverageCopier(),
    BackStabber(),
    BetterAndBetter(),
    Bully(),
    BurnBothEnds(),
    BushMosteller(),
    Calculator(),
    Capri(),
    CautiousQLearner(),
    CollectiveStrategy(),
    ContriteTitForTat(),
    Cooperator(),
    CooperatorHunter(),
    CycleHunter(),
    CyclerCCCCCD(),
    CyclerCCCD(),
    CyclerCCCDCD(),
    CyclerCCD(),
    CyclerDC(),
    CyclerDDC(),
    DBS(),
    Darwin(),
    Defector(),
    DefectorHunter(),
    DelayedAON1(),
    Desperate(),
    Detective(),
    DoubleCrosser(),
    DoubleResurrection(),
    Doubler(),
    DynamicTwoTitsForTat(),
    EasyGo(),
    EugineNier(),
    EventualCycleHunter(),
    EvolvedANN(),
    EvolvedANN5(),
    EvolvedANNNoise05(),
    EvolvedFSM16(),
    EvolvedFSM16Noise05(),
    EvolvedFSM4(),
    EvolvedFSM6(),
    EvolvedHMM5(),
    EvolvedLookerUp1_1_1(),
    EvolvedLookerUp2_2_2(),
    EvolvedAttention(),
    FirmButFair(),
    FirstByAnonymous(),
    FirstByDavis(),
    FirstByDowning(),
    FirstByFeld(),
    FirstByGraaskamp(),
    FirstByGrofman(),
    FirstByJoss(),
    FirstByNydegger(),
    FirstByShubik(),
    FirstBySteinAndRapoport(),
    FirstByTidemanAndChieruzzi(),
    FirstByTullock(),
    FoolMeOnce(),
    ForgetfulFoolMeOnce(),
    ForgetfulGrudger(),
    Forgiver(),
    ForgivingTitForTat(),
    Fortress3(),
    Fortress4(),
    FrequencyAnalyzer(),
    GTFT(),
    GeneralSoftGrudger(),
    GoByMajority(),
    GoByMajority10(),
    GoByMajority20(),
    GoByMajority40(),
    GoByMajority5(),
    Golden(),
    Gradual(),
    GradualKiller(),
    Grudger(),
    GrudgerAlternator(),
    Grumpy(),
    Handshake(),
    HardGoByMajority(),
    HardGoByMajority10(),
    HardGoByMajority20(),
    HardGoByMajority40(),
    HardGoByMajority5(),
    HardProber(),
    HardTitFor2Tats(),
    HardTitForTat(),
    HesitantQLearner(),
    Hopeless(),
    Inverse(),
    InversePunisher(),
    KnowledgeableWorseAndWorse(),
    LevelPunisher(),
    LimitedRetaliate(),
    LimitedRetaliate2(),
    LimitedRetaliate3(),
    MEM2(),
    MathConstantHunter(),
    Michaelos(),
    Momentum(),
    NTitsForMTats(),
    NaiveProber(),
    Negation(),
    NiceAverageCopier(),
    OmegaTFT(),
    OnceBitten(),
    OppositeGrudger(),
    OriginalGradual(),
    PSOGambler1_1_1(),
    PSOGambler2_2_2(),
    PSOGambler2_2_2_Noise05(),
    PSOGamblerMem1(),
    Pi(),
    Predator(),
    Prober(),
    Prober2(),
    Prober3(),
    Prober4(),
    Pun1(),
    Punisher(),
    Raider(),
    Random(),
    RandomHunter(),
    RandomTitForTat(),
    RemorsefulProber(),
    Resurrection(),
    Retaliate(),
    Retaliate2(),
    Retaliate3(),
    RevisedDowning(),
    Ripoff(),
    RiskyQLearner(),
    SecondByAppold(),
    SecondByBlack(),
    SecondByBorufsen(),
    SecondByCave(),
    SecondByChampion(),
    SecondByColbert(),
    SecondByEatherley(),
    SecondByGetzler(),
    SecondByGladstein(),
    SecondByGraaskampKatzen(),
    SecondByGrofman(),
    SecondByHarrington(),
    SecondByKluepfel(),
    SecondByLeyvraz(),
    SecondByMikkelson(),
    SecondByRichardHufford(),
    SecondByRowsam(),
    SecondByTester(),
    SecondByTidemanAndChieruzzi(),
    SecondByTranquilizer(),
    SecondByWeiner(),
    SecondByWhite(),
    SecondByWmAdams(),
    SecondByYamachi(),
    SelfSteem(),
    ShortMem(),
    SlowTitForTwoTats2(),
    SneakyTitForTat(),
    SoftGrudger(),
    SoftJoss(),
    SolutionB1(),
    SolutionB5(),
    SpitefulTitForTat(),
    SpitefulCC(),
    Stalker(),
    StochasticCooperator(),
    StochasticWSLS(),
    SuspiciousTitForTat(),
    TF1(),
    TF2(),
    TF3(),
    ThueMorse(),
    ThueMorseInverse(),
    Thumper(),
    TitFor2Tats(),
    TitForTat(),
    TrickyCooperator(),
    TrickyDefector(),
    TrickyLevelPunisher(),
    TwoTitsForTat(),
    UsuallyCooperates(),
    UsuallyDefects(),
    VeryBad(),
    Willing(),
    WinShiftLoseStay(),
    WinStayLoseShift(),
    Winner12(),
    Winner21(),
    WorseAndWorse(),
    WorseAndWorse2(),
    WorseAndWorse3(),
    ZDExtort2(),
    ZDExtort2v2(),
    ZDExtort3(),
    ZDExtort4(),
    ZDExtortion(),
    ZDGTFT2(),
    ZDGen2(),
    ZDMem2(),
    ZDMischief(),
    ZDSet2(),
    e()
]

axelrod_second_tournament_strategies = [
    # Baseline strategies used in the second tournament
    Random(),
    TitForTat(),
    
    # Specific submissions to the second tournament
    SecondByAppold(),
    SecondByBlack(),
    SecondByBorufsen(),
    SecondByCave(),
    SecondByChampion(),
    SecondByColbert(),
    SecondByEatherley(),
    SecondByGetzler(),
    SecondByGladstein(),
    SecondByGraaskampKatzen(),
    SecondByGrofman(),
    SecondByHarrington(),
    SecondByKluepfel(),
    SecondByLeyvraz(),
    SecondByMikkelson(),
    SecondByRichardHufford(),
    SecondByRowsam(),
    SecondByTester(),
    SecondByTidemanAndChieruzzi(),
    SecondByTranquilizer(),
    SecondByWeiner(),
    SecondByWhite(),
    SecondByWmAdams(),
    SecondByYamachi()
]

axelrod_first_tournament_strategies = [
    # Baseline strategies used in the first tournament
    Random(),
    TitForTat(),
    
    # Specific submissions to the first tournament
    FirstByAnonymous(),
    FirstByDavis(),
    FirstByDowning(),
    FirstByFeld(),
    FirstByGraaskamp(),
    FirstByGrofman(),
    FirstByJoss(),
    FirstByNydegger(),
    FirstByShubik(),
    FirstBySteinAndRapoport(),
    FirstByTidemanAndChieruzzi(),
    FirstByTullock()
]


def match_axl(player1, player2, rounds, noise=0):
    match = axl.Match((player1, player2), turns=rounds, noise=noise)
    result = match.play()
    for i in range(len(result)):
        result[i] = (result[i][0] == axl.Action.C, result[i][1] == axl.Action.C)
    return result


# print(match_axl(axelrod.TitForTat(), axelrod.Grudger(), 200))
# print(score(match_axl(axelrod.TitForTat(), axelrod.Grudger(), 200)))
# print(match_axl(axelrod.TitForTat(), axelrod.FirstByJoss(), 200))
# print(score(match_axl(axelrod.TitForTat(), axelrod.FirstByJoss(), 200)))

def round_robin_axl(strategies, rounds):
    results = {}
    for keys in strategies.keys():
        results[keys] = 0
    strategy_names = list(strategies.keys())
    for i in range(len(strategy_names)-1):
        for j in range(i+1, len(strategy_names)):
            name1 = strategy_names[i]
            name2 = strategy_names[j]
            strat1 = strategies[name1]()
            strat2 = strategies[name2]()
            match_hist = match_axl(strat1, strat2, rounds)
            score1, score2 = score(match_hist)
            results[name1] += score1
            results[name2] += score2
    return results
