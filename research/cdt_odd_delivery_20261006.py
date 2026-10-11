"""Read-only provenance checks; never executes or imports frozen producers.

This is a file delivery audit, not a proof of numerical irrationality.
"""
from pathlib import Path
import hashlib
import json
import re
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / 'research'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def local(name, folder=RESEARCH):
    path = (folder / name).resolve()
    assert path.is_relative_to(ROOT), str(path)
    assert path.is_file(), str(path)
    return path


previous = json.loads(local('period_holonomy_delivery_20261005.json').read_text(encoding='utf-8'))
frozen = []
for key in ['frozen_previous_reports', 'frozen_previous_scripts_and_certificates']:
    for item in previous[key]:
        path = local(item['file'])
        actual = sha(path)
        assert actual == item['sha256'], item['file']
        frozen.append({'file': item['file'], 'sha256': actual, 'unchanged': True})

# The previous delivery also pinned its own reports, review, scripts, and
# certificates. Preserve those 16 files as well as its 64 earlier inputs.
previous_own_pins = [
    (previous['main_report'], previous['main_report_sha256']),
    (previous['written_review'], previous['written_review_sha256']),
]
for item in previous['reports']:
    for kind in ['report', 'script', 'certificate']:
        previous_own_pins.append((item[kind], item[kind + '_sha256']))
for kind in ['script', 'certificate']:
    item = previous['main_integral_classification_certificate']
    previous_own_pins.append((item[kind], item[kind + '_sha256']))
assert len(previous_own_pins) == 16
for name, expected in previous_own_pins:
    actual = sha(local(name))
    assert actual == expected, name
    frozen.append({'file': name, 'sha256': actual, 'unchanged': True})
assert len({item['file'] for item in frozen}) == 80

# Final fingerprints supplied by the authors and independent reviewers.
# These are read-only checks, including certificates with no self-pins.
current_frozen_pins = {
    'cdt_odd_level20_frobenius_20261006.md': '1debc979330f0845b29b09cbd1958a2f2e9b5e5fa59ed795445d76e9cdb3fe50',
    'cdt_odd_level20_frobenius_20261006_verify.py': '8fb171eebc08a00966c4a8affb44dc26b089aa0fee65a801e91b3564fc6533fe',
    'cdt_odd_level20_frobenius_20261006_verify.json': '78655a3a2a822280e90ae60c500501504be83a1919c5cd22e664bb19b3697327',
    'cdt_odd_level20_frobenius_review_20261006.md': '2a93d4d2f9c03a65e37635dd4fa4af6cb0f53a047d3fd6beffeb415e68c4afa7',
    'cdt_odd_level20_third_layer_20261006.md': '89f8a2f0b133c36816e6b434c520b9de7ceae67b0c7dfc03ce18a3334670c885',
    'cdt_odd_level20_third_layer_20261006_verify.py': '148b801fb8816d2e1620263ec8bf304e0d39a0cc4ddf94ce62fdbcd7426218cd',
    'cdt_odd_level20_third_layer_20261006_verify.json': 'a88b0c33e1dc714e44c486b1440b3c4db343ee1be5800e97c641143cb2e93633',
    'cdt_odd_level20_third_layer_review_20261006.md': 'ef2c79ba6e5696da5908dab7f6c3e676450586415c5d3e542b0ab95ffbaba217',
    'cdt_odd_level20_square_lift_20261006.md': '3ce26afeed1e3730cde35d5901e8e148f9e00cd787e7c14c11a47bed78438229',
    'cdt_odd_level20_square_lift_20261006_verify.py': '5cb7dd2ad854d1294556328d824fa30574f0d0653d5e3623ede68004a8452d85',
    'cdt_odd_level20_square_lift_20261006_verify.json': '667c896a32a52ff815e53afb4a3e8b6b79d7cd92f1b1e4de98c9ebf5955099b1',
    'cdt_odd_level20_squarelift_review_20261006.md': '1ce30dba98dc79298cb8385427febb9cfda3bb0e385289e2a5daff8a0ffaa258',
    'cdt_odd_level20_fixed_source_ceiling_20261006.md': 'e6491593755853064edb5bb15edc3abe6260f861e497c1f869d5b3f8e37a56f8',
    'cdt_odd_level20_balanced_smith_bridge_20261006.md': '595e22bfe3fe1fb8edbaa1287cc34a944d7bdd4c9c7a77868b9f1cf12c33ce9c',
    'cdt_odd_level20_balanced_smith_bridge_20261006_verify.py': '0482f56c549b81a187f9a0682a14587a6eea139f7036fd214fdd67f60c28a323',
    'cdt_odd_level20_balanced_smith_bridge_20261006_verify.json': '9682f62c2e5d6e5112158bfb19c1094f42dc5f686378b4f0c20b8b55d0e1cc81',
    'cdt_odd_level20_universal_s2_20261006.md': '0534f29834b6068bed6e49174098de401461492e6913051b0f41285056714465',
    'cdt_odd_level20_universal_s2_20261006_verify.py': 'd9858d18bed21d93fa96544c3187d3e76fb41684e045c4b0d226a6ad1f574d5f',
    'cdt_odd_level20_universal_s2_20261006_verify.json': 'b40c3f999dc5ac9ae1f0cae569e3b947a569d7450ab3304629c63a14f675e476',
    'cdt_odd_level20_large_prime_net_20261006.md': 'e9587ed2814c7e872b7a3b11914564612487f4c8077a165b675778b46a748575',
    'cdt_odd_level20_large_prime_net_20261006_verify.py': 'd645bbf731e174034a7162fe4ba5d5be5a1e1dadf10d8abcfa434fb6ab37ee24',
    'cdt_odd_level20_large_prime_net_20261006_verify.json': '53b811407537feeab018a7ec615dc534e1afc14fbab33fb2f13d79b1d763810f',
    'cdt_odd_level20_squarelift_modp3_obstruction_20261006.md': '23fc9a9b37523c3727e9e54591ebd86ba3e7a55e7474694f337a6a3dfcb98e4c',
    'cdt_odd_level20_squarelift_modp3_obstruction_20261006_verify.py': '50ef8f0acbc98aad4a8ccc7d76aa0e8511743628c7178f0cd36e343cf8eaf818',
    'cdt_odd_level20_squarelift_modp3_obstruction_20261006_verify.json': '45d0d785bcee43a0805ed8aa9686ad9750669095c260ed6eeb02db30d71b9b43',
    'cdt_odd_level20_integrated_tensor_bridge_20261006.md': 'cd93b9f4363f1cd8a065315ef2bbd141e7781d700619549eb23cd693fa68e045',
    'cdt_odd_level20_integrated_tensor_bridge_20261006_verify.py': 'bdd943e711a83e468a2ad002ca7132556e199f6fe598a1b0f85859ec5152a64f',
    'cdt_odd_level20_integrated_tensor_bridge_20261006_verify.json': '77ee147d37b8403c646045be95076676225c4b6374695f33db739a207b6656f3',
    'cdt_odd_level20_large_prime_smith_probe_20261006.md': 'fa79e4044fe1ee0fc6d7572c517046b247679b0c6d1b2c03fc46e968cf442e63',
    'cdt_odd_level20_large_prime_smith_probe_20261006.py': '20345c6596eac48381857ededf29f33eb70a09433772f5c731d2868cf9259420',
    'cdt_odd_level20_large_prime_smith_probe_20261006.json': '8d37f844a5820d61190e3b83baf55694c22f3788e6d99b8c27a9bae2e525e11d',
    'cdt_odd_level20_post_smith_budget_20261006.md': '0c63edbec81ac4a7969b135300dd37c809705cf92b678e51dbc16076fb6d1592',
    'cdt_odd_level20_post_smith_budget_20261006_verify.py': '7aa3b0498222117ce049c8baa26d1b0bafe3a48a3f3f39208517957746407f32',
    'cdt_odd_level20_post_smith_budget_20261006_verify.json': '8cce6dd3742705dbb54210435e2582c265ff6b0e90ba7cca020048994cb1d909',
    'cdt_odd_level20_target_integral_20261006.md': '6c406c7477ec91e944c898a4c9e43bdad98b44acdfa333e674fe539d5c373cf1',
    'cdt_odd_level20_target_integral_20261006_verify.py': 'f552a4b6657ced7890f40faa0f6539548686e03a9ca40943c3a3ada23db7337e',
    'cdt_odd_level20_target_integral_20261006_verify.json': '3213ab1a22bd13b20890a0ea0bc228c8b4497797f8d1239f6b419f4ed30268dc',
    'cdt_odd_level20_cartier_kernel_20261006.md': '3fb70b6b5a744f574e322edf155d6c6a9e2815403d3b8ccf31a139dd4a9aabef',
    'cdt_odd_level20_cartier_kernel_20261006_verify.py': 'dfdf4322755dd2f87c1964c2d48613e269c740255815b2e050e5773aeabbe597',
    'cdt_odd_level20_cartier_kernel_20261006_verify.json': '59fbdcbdf04c8eca23fdde935c0a60a2558f3e1fb91beb6d46f51071a24d8235',
    'cdt_odd_level20_cartier_primary_input_20261006.md': '5d0a04605b08d7b1ce183148e52262da1aa159a28f649be5aec6a9837e57948e',
    'cdt_odd_level20_cartier_primitive_leaf_20261006.md': 'c3861fa5de877e696227db1caa784aaecb848225f5e1fede3477e505ccccdefe',
    'cdt_odd_level20_cartier_cohomology_20261006.md': '399e32e81788f5c59805a38351729b26429bfa25c89d6e803197b10aa7a8470e',
    'cdt_odd_level20_cartier_cohomology_20261006_verify.py': 'd40b86d04c9232a6a647c7108a6233179778efba4ec4b84c669b056528db91a0',
    'cdt_odd_level20_cartier_cohomology_20261006_verify.json': '5bc9fd11ecca5bb7937d15171e5a360e6d0c04cf23f2c3d3093c07bd7f1932ef',
    'cdt_odd_level20_cartier_source_elimination_20261006.md': 'f93170ba6ef4110b4812687550a66017234b5c3cd926262cce38177f2c41668e',
    'cdt_odd_level20_cartier_source_elimination_20261006_verify.py': '271d0b19ae0e2bdda7f1656b98347eb23fa8debc8350949482e61574bc7d6be4',
    'cdt_odd_level20_cartier_source_elimination_20261006_verify.json': '41aa13b31181edd653449bf6266b975217823a2b29d7d75e0b340545383b271b',
    'cdt_odd_level20_hecke_space_20261006.md': '39fb5202d128e45e7881b24ca74d711cc7c68a90f0d5ea11db8217a4cb63ec13',
    'cdt_odd_level20_hecke_space_20261006.py': 'f5df751c007307a8c82598398ae140f588a34b30e20622a4e2d8723baf030fa8',
    'cdt_odd_level20_hecke_space_20261006.json': 'aa3e6b393c4d64c15f3e77b21f3260bed4445175cf0076c347a134b51685ed1a',
    'cdt_odd_level20_cartier_rank19_budget_20261006.md': '47343f7cadff75a294af51286491da9d46a894965767ee47aa2b1af3e8cef81b',
    'cdt_odd_level20_cartier_rank19_budget_20261006_verify.py': 'ec57bd749cd9d0f690f8ecd86ede00626f4d3acd6b6fb19dea4dbffe0e2ae2a9',
    'cdt_odd_level20_cartier_rank19_budget_20261006_verify.json': '6d7d032f7618e1f27cc8621522275a82c5c350afa35ccd36e54d79056d66a94e',
    'cdt_odd_level20_cartier_packet_matrix_20261006.md': '9d21253ca5734191d993090dacee2048641021af0cb961ed27f272ad6a4921d8',
    'cdt_odd_level20_cartier_native_rank_20261006.md': '8c7bbc8e625ee385223e249e9829ac64c045520612a98eb645e67c63dfd69d1d',
    'cdt_odd_level20_cartier_packet_s2_20261006.md': '353d3b3b3763ac52a8e8fa40fb0ca0a8c32b19c4edb85779b9ee74ce74f83a68',
    'cdt_odd_level20_cartier_large_prime_baseline_20261006.md': 'caee882dcd449ece48835d616230efe237ff53d1c6f7f752ac48931d5fa274ba',
    'cdt_odd_level20_cartier_native_s1_budget_20261006.md': '07a70e3cda712cf3bfcbc7d2ce72092d1fbf2e51dcf636ee4aa8971656773ef8',
    'cdt_odd_level20_cartier_native_s1_budget_20261006_verify.py': 'a814f1ff563791dafb82cf81097dc17868490582c359575751b8c232572b06cd',
    'cdt_odd_level20_cartier_native_s1_budget_20261006_verify.json': '3cc24f606d2961e7cea48c5039d10e862f31d27b1d82a22dae735b5a11ad0936',
    'cdt_odd_level20_cartier_rational_primitive_20261006.md': 'ea349dc3aae7cc71832dd052877083dd5f6cc80d0e1d35a5b31748f9f8999fe4',
    'cdt_odd_level20_cartier_rational_primitive_20261006_verify.py': '26d4a5c6577ba39d54ba08ae2499437aa5d1dd2413a7d78cdb0393939a4ae1da',
    'cdt_odd_level20_cartier_rational_primitive_20261006_verify.json': 'd8de8ff7913be7faaabd564fee81f7efed129da7227e81e6b4b6534d9585d3ae',
    'cdt_odd_level20_cartier_mixed_bockstein_20261006.md': 'f3e6b1d15bc61d81fbc802de2861d8f3800713242621d2204bf09f8a9fe6e8b7',
    'cdt_odd_level20_cartier_mixed_source_budget_20261006.md': '8d760ee44d4b9ebb372053feb03d6c4020272b5d4cbfc6f2f97326264925893f',
    'cdt_odd_level20_cartier_background_slow_packet_20261006.md': 'e4b3fe1638c61e07e4585c2c6f6285a746337a913734f1a4c48547b4c68a3c0a',
    'cdt_odd_level20_cartier_background_slow_packet_20261006_verify.py': 'fb99447306cdcc4eb7601b994e8adb2a2fd0020102eb879ef366ebaaed27689e',
    'cdt_odd_level20_cartier_background_slow_packet_20261006_verify.json': '3a425ab2934dfedab56f7c0e18958a6eb8847896814727519f9b9589a619d94a',
    'cdt_odd_candidates_5_8_12_20261006.md': 'bac8c7925a66614d92ee662f2ece24bc77a5cc2d80d963ef6a2642147e258ee0',
    'cdt_odd_candidates_5_8_12_20261006_verify.py': 'a58da369b00ef53ae9e524ee175946e23c4f894d5ca43184599d28df3837bdf1',
    'cdt_odd_candidates_5_8_12_20261006_verify.json': '7eac46807de0046bdaaf96511cd296d0273c1ca6456cfc153914ed3949d6d239',
    'cdt_odd_level20_cartier_slow_intersection_20261006.md': '0e0bd1b19556d233ded68c4f7ecf323730a6cfacc5cc96f08a04f0989c450cad',
    'cdt_odd_level20_cartier_slow_intersection_20261006_verify.py': 'db4ad0e587facdc2dff700632d217531dbe53d6ccad5161ee09d1c0ab673fea7',
    'cdt_odd_level20_cartier_slow_intersection_20261006_verify.json': '1f7ad6db52821f29c1e23367a698c02ab798955bba323a4088c2758e74f1b8ce',
    'cdt_odd_level20_cartier_p13_polynomial_20261006.md': 'ed31e70fa5259952642f3e2bae8d3e60565d584eae73503e3705894d7762aca0',
    'cdt_odd_level20_cartier_p13_20261006_verify.py': 'b9dc1c676851b33dd98e7fe61e13a75562a365ad38d2429124add227c2f9f85f',
    'cdt_odd_level20_cartier_p13_20261006_verify.json': '0284871d8e1ab24520e301a1a52f4501ee012aa7f8841700f4216f48357ca3a0',
    'cdt_odd_level20_cartier_poly_k1_20261006.md': '627fb41df134b22cfa59b8b41c2c54c832f43e66824152fafdfd9c4852b67611',
    'cdt_odd_level20_cartier_poly_k1_20261006_verify.py': '9f35e756f53dc357bce15974740e84ccc6d1628a452276bf2731766e7b4b51b2',
    'cdt_odd_level20_cartier_poly_k1_20261006_verify.json': '39aed863945db7d6ae25c3eaf21ee0d3150a4461600a4c81574ce238af98b379',
    'cdt_odd_level8_mixed_embedding_20261006.md': 'a9a61404dd9d4b255c9603dc061afd76dda3a7351666e4b210f490b512498e14',
    'cdt_odd_level8_mixed_embedding_20261006_verify.py': '6bf89ba6e9e0bdf7f98c77c08e3e98928578949fb04a433549e1c40ba0163555',
    'cdt_odd_level8_mixed_embedding_20261006_verify.json': 'beb18504c9a3fef03ab5cbb4dda3ca3a5ca66ec81ec93c1df16591c27bb294e4',
    'cdt_odd_level8_mixed_period_review_20261006.md': 'ece417474d2c4b4537e03b645fa9eccc4c6b8daa3cecef499228f895d8be7cfb',
    'cdt_odd_level8_mixed_period_review_20261006_verify.py': '50d081d8a0c9627106b19363ca95122fadd56aacce7a7fcca342a704aaec6ecd',
    'cdt_odd_level8_mixed_period_review_20261006_verify.json': '93ad2ddfb0503dbe4ea5c4cee00d94a61b023c6562272f301ebab1c229916655',
    'cdt_odd_level8_three_source_projection_20261006.md': '937e85d01b78e01a9dffcf4205842c43505bab8d58498bb09b3e1502c4fc11f2',
    'cdt_odd_level8_three_source_projection_20261006_verify.py': 'ae7a4bbf7e9a40b6229958e7c034726bce2dea1ed007f41f5c180b07c93a16f8',
    'cdt_odd_level8_three_source_projection_20261006_verify.json': '7fef533e443e5b18e27fd43ac2e036ef0ef853d77bff354d1a1f32c233ae0adb',
    'cdt_odd_level12_source_period_20261006.md': 'd6268c40606a394e1112e7a9e5baee580b426408a1707f28de072b985e2363c2',
    'cdt_odd_level12_source_period_20261006_verify.py': 'd132978f3c3eeb60be45e4903d3f3131626e02dd4fd11688fb5ae3190ea3faa3',
    'cdt_odd_level12_source_period_20261006_verify.json': 'c132cc90d7977ba026017a4b42eeeafe2d0b4a225eb7e9633a224e8d310fccd9',
    'cdt_odd_level12_source_period_finite_review_20261006.md': 'abb494468716888761322c9d5387e5d3d17e2c980c23147ff368fdf95407183c',
    'cdt_odd_level12_paired_coordinate_20261006.md': '7d4551bd7019f8751ec81e9100484224d5c0cd807b5afe170eee5945e6c85075',
    'cdt_odd_level12_paired_coordinate_20261006_verify.py': 'b19953ecc11c5ae88e635727c43450eba5ad2b0e263bf2ea2140e732e059bca4',
    'cdt_odd_level12_paired_coordinate_20261006_verify.json': '10544716ded9f7d306c5e7f36e700a1c4294ad961ab9640d4b72628e5ee531cd',
    'cdt_odd_level12_joint_trigger_20261006.md': 'af784c27e2d7ce48cd8c83f1a52951d9e240733c9fd5ccf560c120f97ebfe2c9',
    'cdt_odd_level12_source_family_20261006_verify.py': '4cbaeb95d6a5e26c3bc1adf6b2c205105ec08dcd402603dfd8c4c8bea7789c84',
    'cdt_odd_level12_source_family_20261006_verify.json': '0eae105c87144d53a004a275a613d06ee85f87a30d15be90a3db9adfc8de11e4',
    'cdt_odd_level12_source_denominators_20261006.md': '9451f96b85b4374b443b83aba7e700a61d1ed17abe07df43a3a031f1500f65f7',
    'cdt_odd_level12_full_leaf_20261006.md': 'f0c79d2a0ba5bfebf8b0851ac70834ddac084d742f6912d623d044ba4c851260',
    'cdt_odd_level12_full_leaf_20261006_verify.py': '170ed7cd93eb553b2a320f762ae412fbf99332cbc46bfdb1efbf943c0bb5af79',
    'cdt_odd_level12_full_leaf_20261006_verify.json': 'a33d95f888a117711551b7b6562c95ece7f9f2d8d35fe2d22d8ed15b295f5e5e',
    'cdt_odd_level12_budget_20261006.md': '1e2419b1afd3e24c73985c01a0c166d597a431c9b135af587082a7479848065a',
    'cdt_odd_level12_budget_20261006_verify.py': '06bcd41b975c939ef8bda2c86f362fb6ac1e14f9e177f2dce1e0288901cb1d6d',
    'cdt_odd_level12_budget_20261006_verify.json': '6a7195895c7f8cf4564a842577a67efde72118b9c3d695623b524872570d5aa8',
    'cdt_odd_level12_cheap_log_packet_20261006.md': '2a4ca1f9f3fbe94406e41b8cf10d94456027003962c2893aea88305a9e8d25c3',
    'cdt_odd_level12_cheap_log_packet_20261006_verify.py': '7d9cf323ded9a9127e252f5025cb5b3d5b96351cac3a6dadb78d80a46a7ef860',
    'cdt_odd_level12_cheap_log_packet_20261006_verify.json': '582ba17bd9703c33e44856ff5a8ecd3d00d96c977a8ecd3784c444af9afec115',
    'cdt_odd_level12_cheap_log_transport_20261006.md': 'bd4f42b29e8e5d54c6e05af15153fd08fc07d9ca45ca68e16091f2988847d083',
    'cdt_odd_level12_cheap_log_transport_20261006_verify.py': 'c4e859a8cfe8a4578148e3f4733af109d86361daf079e6bba532b2467336b597',
    'cdt_odd_level12_cheap_log_transport_20261006_verify.json': 'f635a7ff2c9bd0f8665859f419b87f808a8185d66cb782df2df2ce56c954da0a',
    'cdt_odd_level12_hecke_radius_20261006.md': 'd21718cd052ffb2c2945529492bb09450a9aa51363beb261da0e139dd7dc0911',
    'cdt_odd_level12_hecke_radius_20261006_verify.py': '859981d2309a51c7be191dee912c8554ffe45116f30d4a5cc7e56875ee2ecd37',
    'cdt_odd_level12_hecke_radius_20261006_verify.json': '96d9e2abc89bcc3b63d31cd8ed0fac1f630300b812e19fe57833ff2a20a960c2',
    'cdt_odd_level12_augmented_radius_20261006.md': '55db5571fd9c4705a5d16fa11577046249026d3c5b27a21cbd65787fb5edaed9',
    'cdt_odd_level12_augmented_radius_20261006_verify.py': 'b8dc7c5f16c9c43bc094e3afa2f294e6fdac1c18782a26c106ed56d797fb1e7f',
    'cdt_odd_level12_augmented_radius_20261006_verify.json': 'cda6471f2c79bbd0e308d4043961ec46ca10755e092a07bd776ef139a6a3583b',
    'cdt_odd_level12_signed_cocycle_20261006.md': 'a79263cc2c21fc1babd8ce2eef7e4ddbfe17ef70e6a9eab23a6b37a6e3a4f363',
    'cdt_odd_level12_signed_cocycle_20261006_verify.py': 'c5283ec80047ebc3148a6f7b966c343d2ffc88bda82f6bcb0740735186e97e91',
    'cdt_odd_level12_signed_cocycle_20261006_verify.json': '25c877a9a94e85f2e16a16f0a03f4022de968ecabdc1cf7f7667b556149c03ee',
    'cdt_odd_level12_character_tensor_20261006.md': '552fe1e4d48153f3055e1b733542ebae0e4981eb20e20917272c35175a4c2516',
    'cdt_odd_level12_gamma_cocycle_20261006.md': '3dc551274a54640d6d947ae0db4fc920a0bf4463507cad0ed189d5b5197bc863',
    'cdt_odd_level12_gamma_cocycle_20261006_verify.py': '0940f2d5b5aef892991fa8db79606e4b961592a73f21c30ab2191fb7dad43646',
    'cdt_odd_level12_gamma_cocycle_20261006_verify.json': '28874966cb4f8452598e90c16142d39495c1e4bca773573012dbefa689422d94',
    'cdt_odd_level12_schreier_presentation_20261006.md': '92ed43b8a1426c66eb65898b016a38012263ae876e753c1bbae2496d104fff9e',
    'cdt_odd_level12_schreier_presentation_20261006_verify.py': 'ee2fd2a8f084909d8f725209282594715c521bd6e1d3453c07786ced8be2406a',
    'cdt_odd_level12_schreier_presentation_20261006_verify.json': '387b30f338e5231397b905a64a58e5648bae1772af305b8baf9ed28e3b970fe4',
    'cdt_odd_level12_generator_cocycle_20261006.md': 'a3f00c593a9fcc3f9b1791b854faa0ad7b721b6c76d67cc52598cd5f919f67ca',
    'cdt_odd_level12_generator_cocycle_20261006_verify.py': 'a92be40d4f9f789d0ac81ecfb486074c6937509588e9aa51c5d7fceaf5c5307c',
    'cdt_odd_level12_generator_cocycle_20261006_verify.json': 'b8dfb80d30a4fc276d225d148c76ead7032de51523896664f5c743eb0af966ef',
    'cdt_odd_level12_joint_full_model_20261006.md': '9dadea03437be66fb012c4ef98dff6d7f04ab3cdbedad45b57afb481dd957d08',
    'cdt_odd_level12_mixed_log_smith_20261006.md': '3177042b9cc2040fc36305e096a17d591dfcf5c38efe84d44a7dada6bf74a51c',
    'cdt_odd_level12_stabilizer_structure_20261006.md': '7d2d33557945c880857e080cd1ffbfcb22902b4d7f3d7af0fd02e204cbc8cd22',
    'cdt_odd_level12_stabilizer_structure_20261006_verify.py': 'a87b6ad7a14b5bf40a07dc47bf7c073f5355a0a193a838d9f2638a2347d5d8c5',
    'cdt_odd_level12_stabilizer_structure_20261006_verify.json': '00b27e3470516b94e00a996f58fbc38cb7f4472630b97cf0ac2a448daae3737c',
    'cdt_odd_level12_stabilizer_boundary_20261006.md': 'bf3de144a9bf8c1605595ab95000e6b764c3de4652a378a709f7d5d9a63d2168',
    'cdt_odd_level12_stabilizer_boundary_20261006_verify.py': '6f6d06c2ce1e9d5a13ad824437fce5a3f8af8d5c0f343fbad83f51b035efbacf',
    'cdt_odd_level12_stabilizer_boundary_20261006_verify.json': 'd377fd503f25a59ba9509bb6d53435464a64728537aea3adc1f169ae309cfa35',
    'cdt_odd_level12_affine_galois_20261006.md': 'a74ca9ef73f3c4967e97c928ea37f9d1a599ea2dc68d959bdac24d5b042dad11',
    'cdt_odd_level12_affine_galois_review_20261006.md': '2e984dd545a42dbb9f454b936398be42787efd1ebd88f292360fa049d37105ad',
    'cdt_odd_level12_vector_leaf_numerator_20261006.md': '34ab1b84443e88581c64cc88d744835a39bcf1ee4ddb1c59a7335fe95cc00b56',
    'cdt_odd_level12_nongauged_rank_20261006.md': 'f7029b986ec843d916e31eb487c6d1f4196fed47f74465b0c685c1ae8daab6d1',
    'cdt_odd_level12_stabilizer_timelike_conjugates_20261006.md': '91844cb46daf2914f0ddc0e03b6e4eb1bb9db30c44463135bef56eff1046acfa',
    'cdt_odd_level12_stabilizer_mixed_cusp_pair_20261006.md': '8788470a07837cfb81d3cb8c043b2ba6d0eedfe7d50928d0aaaf64bf72b5c570',
    'cdt_odd_level12_stabilizer_mixed_cusp_pair_20261006_verify.py': '139175091c22f8536402c3efa65338c8094ec22542528db07cad57b7fe5bd36f',
    'cdt_odd_level12_stabilizer_mixed_cusp_pair_20261006_verify.json': '9c7c4ff590cb37feab2693546cc9a1238bc85697f8ccb081e58b43d03c10dcef',
    'cdt_odd_level12_stabilizer_signed_powers_20261006.md': '3827f31d881750452060181e5291598ffd2c6542b0a260a2fa9ab37a2a95849e',
    'cdt_odd_level12_stabilizer_parabolic_malnormal_20261006.md': '08191d03fbf81976eec2395b880614235c7e0a1c645d319cc575dc391c7968b0',
    'cdt_odd_level12_stabilizer_parabolic_malnormal_20261006_verify.py': '4f585e84d18b0847d607445d6ce47eeacb985e4dae0a648b92f019bf371b6f35',
    'cdt_odd_level12_stabilizer_parabolic_malnormal_20261006_verify.json': '493d4fb0589a36b2ff09c9b16e3efe8bcf63118f4cb248ad27f59d65a494a6e0',
    'cdt_odd_level12_stabilizer_full_timelike_conjugates_20261006.md': 'e73f054deda9fd3cbba60038c40274c2ecc0e62995cb2fe2d017ca38fff7e691',
    'cdt_odd_level12_hodge_bundle_evaluation_20261006.md': '3ca6afd239177a1a94dab9dd975434d23ba76279ab9049b7e77f1ab83019811a',
    'cdt_odd_level12_zero_period_corrector_family_20261006.md': 'ace4e4e65bee3848ca1849e5068cd1449b86b8a298e28e5d47ca93fcda425ad5',
    'cdt_odd_level12_zero_period_corrector_family_20261006_verify.py': '41675be7f5d5dfed4a432f62eaee1a002b71ca1a7ed9aa16ffd7bc823582c7cf',
    'cdt_odd_level12_zero_period_corrector_family_20261006_verify.json': '8fe2f5ca447d3e08d30c824c51d8c7911e409e317454511659efc25fb9b68f08',
    'cdt_odd_classical_derivative_projection_20261006.md': 'c24a4d7807bed750f63746b4506f2a238a7d9b9122e2e39ac4871653b39d5c1e',
    'cdt_odd_classical_derivative_projection_20261006_verify.py': 'bc15dfe4b9a44cff84be528d556c5ca4ac5080e6790a757e875ac589652b4a14',
    'cdt_odd_classical_derivative_projection_20261006_verify.json': '66885c07c41e8cff3e0d0dbfeb51f931bc4f8ec3aebc2af77773061f24e6fc92',
    'cdt_odd_level12_eisenstein_extension_20261006.md': 'e7a9fe7650820637ae88b68343239e85d2e2dcb6503fe093da90baefdfff631b',
    'cdt_odd_level12_eisenstein_extension_20261006_verify.py': '3f690d0fed8697734926d0e8aaf99711fc624e1b95e8b39f1f8aa006ce3f1d64',
    'cdt_odd_level12_eisenstein_extension_20261006_verify.json': '14fa31fcb0db8ea46690237cc25b7b33d811b0efbc30dfa9c0cfcf2fcdd3b031',
}
current_frozen_pins.update({
    'cdt_odd_classical_spin_pullback_20261006.md': 'a82ac7c4dfc6b3087ea25ad23be8b87fd5330683784402c65839349acb2b229e',
    'cdt_odd_classical_spin_pullback_20261006_verify.py': '0db52340d62984cdef9d5d381717c3ddd13226763bb9470fb5b4509c463eba2d',
    'cdt_odd_classical_spin_pullback_20261006_verify.json': '39c44949f0ecc03c9a2a93940928696a9f723ebd6c5c77f84d7bb311aeb4cfaf',
    'cdt_odd_classical_spin_monodromy_20261006.md': '8987d70f750d1d9d754378fd4e84633e0233ac227fe4f5879eea96fc1be920cb',
    'cdt_odd_classical_spin_monodromy_20261006_verify.py': '097c0bf59c2abccd14438ba34505818a33d0c80bef5edde50ef67a06e446288c',
    'cdt_odd_classical_spin_monodromy_20261006_verify.json': '3713973b1e3907d65b055a8ac465320ab05e9e623baf5ed5193016c478075517',
    'cdt_odd_classical_zeta7_forcing_20261006.md': 'a8d34936cda965923751c748819a6601330e7534616e49245a1264ca8eb91ab4',
    'cdt_odd_classical_zeta7_forcing_20261006_verify.py': '239e265f2582dc356686270ffeb4be9c2a231b6581ad7356a6800d0cf089564d',
    'cdt_odd_classical_zeta7_forcing_20261006_verify.json': '5ff55c13f3c15a1372e029cb1607ccdd5c184fc1e15e78b1cfdc03dfaf06fe90',
    'cdt_odd_classical_zeta7_forcing_spin_20261006.md': 'c3a4212bccdc4dd18331e6a1446cf22dd88462d27b1631c350c12d2f78c9a56a',
    'cdt_odd_level12_corrector_multireflection_20261006.md': '82cf842b2a7067c3491818722e4e851452add097c33a461b0818ce657f618761',
    'cdt_odd_level12_corrector_multireflection_20261006_verify.py': 'c21184b83244ac19256e8861075e0a1d9cdf65e4c6d1cea074512bd0486ced42',
    'cdt_odd_level12_corrector_multireflection_20261006_verify.json': '0bfec8a6767de1998ef1bad84ab4b11aed59ba6e0f4f43437a8fe00d9f440ea7',
    'cdt_odd_level12_corrector_green_budget_20261006.md': 'b520f4199015e509ac1908419e1cfa073c85221f8b7665fd0be19037b2d295e6',
    'cdt_odd_spin_corrector_review_20261006.md': '546831a277b3c7875d12543b2c8c7c7038654344d904c49ee27008fdd90801b6',
})
current_frozen_pins.update({
    'cdt_odd_classical_zeta7_full_rank_20261006.md': 'aa7bcac62a507f2f1ad15aa41d5d8fa4187d667f010a84cf01e89b7265191e0b',
    'cdt_odd_classical_zeta7_full_rank_20261006_verify.py': '19d48a8a83a56d4d89db17d5a8614349a77df6cb2c41f9693e376578fbb9366d',
    'cdt_odd_classical_zeta7_full_rank_20261006_verify.json': '070589b3a70bfeb4c74e66c3dafc1175a8ffd4a1850cf48f252a0198fc4def73',
    'cdt_odd_connection_moments_20261006.md': '061d56790a7e5928268a93174029d8f2ef6b903d17dd6b124e596210f0d1d25e',
    'cdt_odd_level12_cuspidal_corrector_window_20261006.md': '191651c0dcda2306d09f110cc16d525b8babed615516c136436f5e20316de16b',
    'cdt_odd_level12_cuspidal_corrector_window_20261006_verify.py': '1dc4630e3dee281283579c1c9aa8880ef7e4cca2fd0a1343251103733bcdff19',
    'cdt_odd_level12_cuspidal_corrector_window_20261006_verify.json': '7e59a87618d731ce7cc0dee9acfff50c1ef25436ebb6e4ea4fc99b23abdb63e0',
    'archive_cdt_odd_connection_primary_20261006.py': 'ea5549a25427dbc7a86928b737b69b9f342d562b42b418284c6a45947e0481a8',
    'cdt_odd_classical_lambda_leaf_arithmetic_20261006.md': 'fbb9e38e3f8bef23f3cf3940374b97a5d3d7ee6d4ad2ca1dcb0912f88e4211e5',
    'cdt_odd_rank_connection_cusp_review_20261006.md': 'c342d47f198d183a704a2c3dba70d27cf9b316cf8fa46a64d9e2f3e70263de60',
})
current_frozen_pins.update({
    'cdt_odd_bailey_M1_period_20261006.md': 'd2c85099fc6ccc4f16230c141ff7f771b8a5656a62bf81c2c232e07049fe1f90',
    'archive_cdt_odd_bailey_confluence_20261006.py': '53bfce13a1b9073d83d94cd781b91ac8b04afaca126b71bd26b6582f59892499',
    'cdt_odd_classical_conifold_calibration_20261006.md': '81d6c9aaf66dcc75cdec55cd52a9d8f6412d295ee6f14b46673ec8ed3e2bd53d',
    'cdt_odd_classical_conifold_calibration_20261006_verify.py': 'fc901485d61f8802d036fd8fa34aa4beeb877ffc957836c300e769704b712876',
    'cdt_odd_classical_conifold_calibration_20261006_verify.json': '7fc698cadcd2dc1fc8dfabb4603d8d886eaf596546596d2dc90bfeb71642e471',
    'cdt_odd_classical_frobenius_smith_20261006.md': '81e995972aead798f8086fdec2fac9e0afd75debcb10fc058e2862b7f185cf64',
    'cdt_odd_classical_frobenius_smith_20261006_verify.py': 'b1d4d75fe7f300cc39345f8c3a0debe9c7f351b96b2edef52f04cd29001cc581',
    'cdt_odd_classical_frobenius_smith_20261006_verify.json': '6a703cff4b27559174f2bc9767af93d497a25c105679e5f31e3444e7c5332550',
    'cdt_odd_level12_manin_period_interface_20261006.md': '76ff29fad9a7bcb2a26b360dc0feeb24d49723473bd999f41e8eb2d409b619b9',
    'cdt_odd_level12_manin_period_interface_20261006_verify.py': 'f546df287d3c26b63ab77651ed3c80500c7a4897acc84ffdad433c3a534c91d0',
    'cdt_odd_level12_manin_period_interface_20261006_verify.json': 'c5899117de1b98ba23442c14e2d9db70efc53f9ad5637a69d3095c032829af42',
    'cdt_odd_classical_M4_bilateral_reduction_20261006.md': 'be74606c6134072ffd550f50ec87543477fd8ea9404648f1dc7c13e1d988d1ec',
    'cdt_odd_classical_M4_bilateral_reduction_20261006_verify.py': '15eef9a2fb64a8b22d7e12eb35b335260e6257fcc6c6a63faea3a05ebea1b123',
    'cdt_odd_classical_M4_bilateral_reduction_20261006_verify.json': '3241db1c06b66b6508e285cb1229457a257f0434eb070336912d626f9d54e8e9',
    'cdt_odd_calibrated_period_smith_review_20261006.md': '90ec261ff78f5f2a91309d90722520b8afdf90e22d1bb119f00a30ae08af1c32',
})
current_frozen_pins.update({
    'cdt_odd_quarter_shift_full_model_20261006.md': '11e9d6d6c591fa779d44b8552c0f7393d529a348fc27bbb57fe9c09ec71cc51a',
    'cdt_odd_quarter_shift_smith_20261006.md': '495fea2dddf4c40fa021db89c9869a63af6ab6a820bcf98dcfe999381212f709',
    'cdt_odd_quarter_shift_smith_20261006_verify.py': '2b187e133e8be04db27a34a494506f9d77695c94de3640abc4d8054e77ea0ab7',
    'cdt_odd_quarter_shift_smith_20261006_verify.json': '67a9b32fdd805d710b4f2a5574d8c80d36474ac128ed45a82cbb09f05258bb4e',
    'cdt_odd_quarter_shift_independent_review_20261006.md': '5fd6e1324defa2e01ce5f8d5850db30471e01c18eb140a95c118ef02990a795c',
    'cdt_odd_quarter_shift_cost_independent_review_20261006.md': 'a7a56535f4dcce721fbf0ba8230e858d38f5614d811aa9be7fcd216da5de6431',
    'cdt_odd_R0_kummer_period_interface_20261006.md': '803b3eced9825fe5f40005728430188e36c4a8cd123d41223972cceb23c2e172',
    'cdt_odd_R0_kummer_independent_review_20261006.md': 'b39924f27a57c00a3813498c8ebc7ea3b02f342dc4bfa8b1f73db293640f65fa',
    'cdt_odd_level12_trivial_cusp_period_20261006.md': '141be188b94e557f9e1ebc970f1daf3756eb946195885a048c6514667d0140ae',
    'cdt_odd_level12_trivial_cusp_period_20261006_verify.py': 'd994a917e296f1c965d56a7604508a2b235e883381db58b41feac53be633ba8e',
    'cdt_odd_level12_trivial_cusp_period_20261006_verify.json': '73672b7eb3be34503ff8a77d03549752b3cbff6054fd7f20f23d8f0725fb4ad6',
    'cdt_odd_ehmm_special_fiber_targets_20261006.md': 'ad3bcafc91c03dd30e31053ae5a2ac005f78702cfd23f5faa176d4a413e3c900',
    'cdt_odd_quarter_kummer_three_source_review_20261006.md': '3b2f8cdcf70e9ded1d06ba6d51691a0482a30522e5d1920fd7ef8f932184b41f',
})
current_frozen_pins.update({
    'cdt_odd_complete_F_high_filtration_20261006.md': '783397a97c19de4caeb65d0edc9e2d912f27e9ebddf9090c7915dbf90a49bbdc',
    'cdt_odd_complete_F_cost_bridge_20261006.md': 'a304c7eb60f99ad859130bdcb2a7799292ccdb9cc9563de3f6a30c6f3599e149',
    'cdt_odd_complete_F_cost_independent_review_20261006.md': '1d3fb3d3f98756f5be61d223feaf57c17fa199e071ce52deba2afe8a9d4b889d',
    'cdt_odd_complete_F_R0_independent_review_20261006.md': '430e1a58c3688bfe5966c17b7be61e96cc1d55298ef8e7356066e9effb5d0640',
    'cdt_odd_complementary_quarter_period_product_20261006.md': 'c8455d668454524518efee01ad95f6ab19f5817210022302c9a5f8baddbb1266',
    'cdt_odd_quarter_product_rank19_interface_20261006.md': 'e1deb97098eaf3521506560d2aec824a0ad8fd2c1700041c806705aebcce11ad',
    'cdt_odd_rational_conifold_projection_20261006.md': 'c242500f7645a188714538d51906b2c9f285061a6b045abe0ddddbb373d424c4',
    'cdt_odd_R0_relative_cycle_mirror_20261006.md': '43009e569bba25b6f819f0e5f1de0b96fa2db57e1a73817e8b087d294a059912',
    'cdt_odd_R0_relative_cycle_independent_review_20261006.md': '312d6905e9896f25214c9f85c509ecfebb4bfce2e69456e509383f928c4e6f26',
    'cdt_odd_integral_cycle_full_F_product_review_20261006.md': '5316b8c738c651a98fe66a240ecf7a14a547051eaa8e767b48eea798b82446ef',
})
current_frozen_pins.update({
    'cdt_odd_quarter_product_actual_rank19_20261006.md': '55adb223c226956a47a082eace77190ef7fe2d153f932494c68db8414ae72189',
    'cdt_odd_quarter_product_mixed_packet_20261006.md': 'fdbff4b3b35d1a8c6e69f47613ee584017723e6a2ccfd2f40ef5305abbde8e1d',
    'cdt_odd_quarter_product_mixed_packet_20261006_verify.py': 'aa415f8f33e28184d4bd2701820bdaaf68a42aeea287fdecd19ba2b6983f0f7e',
    'cdt_odd_quarter_product_mixed_packet_20261006_verify.json': 'cc1ad92a76fb662a765ec7b63d16feb87f4b033955d6c3e7a31f58ec1ad1f86e',
    'cdt_odd_conifold_arithmetic_center_20261006.md': '10c1e882a7cc75b2f8b6be82ed6c241ec3900db07109ff144c041cc734f3e7b0',
    'cdt_odd_conifold_arithmetic_center_20261006_verify.py': 'f2f0e3e9ffb785abb5f5a315590f0885f0f5964846975d1101c98b170f6236d1',
    'cdt_odd_conifold_arithmetic_center_20261006_verify.json': '7bc10a6760d84c69f879b0c1dbee77a00b3bc3c647edb27d91aee2ee734fa911',
    'cdt_odd_conifold_arithmetic_center_independent_review_20261006.md': '24da335b5e1598d28d1f59f2b38285bb3e8135d7d4ba3d2cfb7189d0d7a0fd83',
    'cdt_odd_quarter_actual_rank19_independent_review_20261006.md': '05bde1674d2ca7bee517eb10e79ca9c20fc985fa6e772d3c8cc39412a398d074',
    'cdt_odd_quarter_actual_rank_mixed_independent_review_20261006.md': 'e9f0f994b954d69904e18a91f87b5f026158a6faaac415c0a3872af39df1d751',
    'cdt_odd_R0_toric_completion_20261006.md': 'abbb47907e85e2ae15c12bfaa6655f8f25497e804e299e15bd9277e7a6a667b0',
    'cdt_odd_toric_completion_conifold_center_root_review_20261006.md': 'ce97c792d30e32d677bf432c68b02b5bad09571dd599cc24349dbfa4eda43965',
    'cdt_odd_R0_toric_completion_independent_review_20261006.md': '29c2aa899cb008c642e6de4f2a24e437431591f2a5eb3685c13fd919768baeaf',
    'cdt_odd_R0_toric_completion_uniqueness_20261006.md': 'b6baab390cd23c15b1edc717e11a3b97c42dfc4f5c16a8c87c10fe74676f66a2',
    'cdt_odd_R0_boundary_completion_uniqueness_independent_20261006.md': '8a82454febe2ac52ff179ed79338c17c940fea3e76ca071afe38a23d6fcd02b2',
    'cdt_odd_R0_toric_uniqueness_author_independent_review_20261006.md': 'ed3e31211e09ec33142558fa5c12bcc972c7735174b190d3983049d533659a9d',
})
# NEW regulator/compact-period round: previous pins remain unchanged.
current_frozen_pins.update({
    'cdt_odd_R0_klm_current_interface_20261006.md': '58efd06503589a35b442b4cd60625741514b51cf183308f1a9ef4a1ebf053e3a',
    'cdt_odd_R0_regulator_derivative_20261006.md': '5a3ba4ed679a5565375efdb0b9c39e4a69338e72bcce5938b5a34356d816e091',
    'cdt_odd_R0_Yukawa_scalar_interface_20261006.md': '172a0830a547fd3d018953ca996ca6c5d2d67ace172a9943acee6c1cc9044b15',
    'cdt_odd_R0_positive_cut_period_comparison_20261006.md': 'fb44cacdd85484887a51c90c7547432eff5ceb0516b356a3fbc26a5f97f65dc8',
    'cdt_odd_R0_regulator_yukawa_root_review_20261006.md': '99d1965a15296af0a3b70b256247939ed962ec051a53c40a2022dcfc9346d8ef',
    'cdt_odd_R0_positive_cut_period_comparison_independent_review_20261006.md': '421adc464920aadb9a9a16d917a2d5e070bc7ac56eaef31775fe91ec4965d3a0',
    'cdt_odd_R0_Yukawa_independent_review_20261006.md': '6207c36f8939dd6d46e9071a9b52e96672862b7abb01dbd042ed3b6e53812af0',
})
current_frozen_pins.update({
    'cdt_odd_R0_vanishing_regulator_normalization_20261006.md': '7a254a5d974379a76142aee36120390d5dbd7491c4794d97997976d082cbf296',
    'cdt_odd_R0_compact_positive_cut_class_20261006.md': '094aa342bb462a080c99b525110e8b1738acb58897aa2e4fbe9aa991a521c5d7',
    'cdt_odd_R0_boundary_membrane_comparison_20261006.md': '2bded7f6e0e6efab5e67f985df38754e5a8b2f99b4e4394d46a6f86a20952c3d',
    'cdt_odd_R0_conifold_actual_arithmetic_hypotheses_20261006.md': '83e5fb5cb3e7cad72440d04e4f75230c895d2865bc68c1565160a6c3b313d567',
    'cdt_odd_R0_vanishing_regulator_normalization_independent_review_20261006.md': '8fc3344968a3ccfe24f652912d77e46d5527180db5c69f6520b9c40bb8950545',
    'cdt_odd_R0_boundary_membrane_comparison_independent_review_20261006.md': 'b5ee2661ce00122f94e232ec4c82547c6737239b9210d8ad8fbf9c94c64ad3b7',
    'cdt_odd_R0_conifold_actual_arithmetic_hypotheses_independent_review_20261006.md': '1f81569b7fa5141966654c797e015fc4f1c9997d79c8f5e76a1d360c35a4da8b',
    'cdt_odd_R0_current_cycle_arithmetic_root_review_20261006.md': '2ee23b6b4c3c5c6e08e3741b9887fb729bed0b458092919fbb00a72224d4218e',
})
# NEW centered-current/real/exterior round: all previous337 pins remain unchanged.
current_frozen_pins.update({
    'cdt_odd_R0_noncompact_Tate_boundary_period_20261006.md': '00d1cb69f8cf783b842dd5c53331368bcf95fddf69135e80f614c4f0598372c1',
    'cdt_odd_R0_positive_cut_boundary_flux_20261006.md': '3fabdbfa3f4c0fd17e50db268b86cfe8c7d752f71a462bcdf0ebaeb1faa3d150',
    'cdt_odd_R0_real_Betti_normalization_20261006.md': 'dd541870010dc296993f512252e6b359bec2a1c147b382d288637078ef9c490f',
    'cdt_odd_R0_endpoint_sensitive_exterior_packet_20261006.md': 'b02f39ae453143b72572bef7e91e53697bed90388108e79b267e27168dae96ef',
    'cdt_odd_R0_noncompact_Tate_boundary_period_independent_review_20261006.md': '652483276ee0e98787e792822243c3842aa1b2dec27594fbf144aee570fec5b6',
    'cdt_odd_R0_positive_cut_boundary_flux_independent_review_20261006.md': '7cfbcce37c932b1ecd8b734ceaf8993d1c383798ee25c59958c6fb857b731b16',
    'cdt_odd_R0_endpoint_sensitive_exterior_packet_independent_review_20261006.md': '0ff0e13e00142733e81587bcc11e2b1bcbd3040e057b4d6b613ea8a8c9f940d0',
    'cdt_odd_R0_boundary_real_exterior_root_review_20261006.md': '47352a518783b9902e0350af76108b1b2c32b69430cf24b7cf03a13e76042021',
})
# NEW integral-lattice/dyadic/holonomy round; preserve all345 earlier pins.
current_frozen_pins.update({
    'cdt_odd_R0_conifold_effective_denominator_20261006.md': 'fea01700aa99716201ad0e36b161557f98f8e783755d7bfe144f434d1d59d3f8',
    'cdt_odd_R0_conifold_effective_denominator_20261006_probe.py': '6bae4c3b34b3bb006fa6a6b697251d8a9ff4543c797693ec4414eb66f1a27c6f',
    'cdt_odd_R0_conifold_effective_denominator_20261006_probe.json': 'b275f2481c3f02b571ccadd447d5a776d58842eaa2614bde5c67ecb0bb801ebf',
    'cdt_odd_R0_conifold_effective_denominator_20261006_symbolic_verify.py': '7ac54b6094f4346673c1a931ced683fbf7143fe162af6b5caa200f01e48c1c01',
    'cdt_odd_R0_conifold_effective_denominator_20261006_symbolic_verify.json': '305eb28b0d38bef698b02ae7871dc54e65b359742d310f7909022d1a0abfbc34',
    'cdt_odd_R0_actual_vanishing_orbit_lattice_20261006.md': 'baf29ee041a0ea48c4b64c517cf0712f24c52c4c98893e4c74a98698c7e05586',
    'cdt_odd_R0_actual_vanishing_orbit_lattice_20261006_verify.py': '0f00023b927881f1cf824be2e50b1177dde6654a8db7799eb98538697b044dc0',
    'cdt_odd_R0_actual_vanishing_orbit_lattice_20261006_verify.json': '4449759efb4a051e406daa83e411fb3b67940f1b612cf7b9af0a42dfbf6eb02b',
    'cdt_odd_R0_regulator_Betti_extension_flag_20261006.md': '4abdcbc370b69413b07e837724867897760f493b7ee65e6d0b47a705f96292f4',
    'cdt_odd_R0_endpoint_flag_holonomy_interface_20261006.md': 'af728ecbebe3ac4827f7388706d4c5892896437e625e1bf4a0671b949bff28b5',
    'cdt_odd_R0_toric_odd_prime_smooth_model_20261006.md': 'bde766ee2c7825c9b7a3de7bb77ee4a2b42983a51ab2fc8f6bd28c9cb16e323d',
    'cdt_odd_R0_actual_vanishing_orbit_lattice_independent_review_20261006.md': '762a1da5b4a155ae63b442bbe4396c28ebbf8eef9a4b60933d73d3409ad6c08a',
    'cdt_odd_R0_Betti_denominator_independent_review_20261006.md': 'e7eb97abc1de58de3a557fb4748b32450d4785217d5895ca07d5b9915abdd5fa',
    'cdt_odd_R0_actual_Betti_integer_lattices_independent_review_20261006.md': 'ea21720676ed8dad198de7ee6e34a354647699f85f4c826d941c19ef3b82e9dc',
    'cdt_odd_R0_endpoint_flag_holonomy_independent_review_20261006.md': '5b842cb2c88380a483cc1b8135dae341751be94c5a34d95b0629e8ed7dd342fa',
})
current_frozen_pins.update({
    'cdt_odd_R0_all_odd_generic_radius_arithmetic_interface_20261006.md': '439a21b2bdf35eeffcbf46e016b35e6ad3b11b635baa8e4148d6533741f6dc5a',
    'cdt_odd_R0_all_odd_radius_independent_review_20261006.md': 'b2cb52c650e517ed3aff06e554747e77f21ef8aea1d22e5c078529a837ca09ef',
    'cdt_odd_R0_all_odd_generic_radius_independent_review_20261006.md': '0acd3455023cfbf825283a9d11941422327efdf5e0e6d2080120d0bf40305e09',
    'cdt_odd_R0_dyadic_number_field_scale_supplement_20261006.md': '5a800387513a2f6593087991d5371dbfca47eb8c6c1b74971fe13e3965f4c2b3',
    'cdt_odd_R0_integral_flag_denominator_holonomy_root_review_20261006.md': 'a41ea5dc5345608dba3d70c316894514b0e2cc99f60c91314d64ea4bdbff747b',
    'cdt_odd_R0_dyadic_number_field_scale_independent_review_20261006.md': '005432bea72be1376098814bc0b3f5c74f6ca24058d200e841815409a129dcbe',
})
current_frozen_pins.update({
    'cdt_odd_R0_origin_orbit_mod8_obstruction_20261006.md': 'a510202c396b90fd95abc99fbba950cf6a8a53870f01b769a336ee380bf756dc',
    'cdt_odd_R0_nonlinear_projective_invariant_field_20261006.md': 'ec6ad8fedb27a1eea5fcbcdc8afed0b58a4e13cf6a393568c8274c9d16afd59b',
    'cdt_odd_R0_logarithmic_flag_slopes_reduction_20261006.md': 'aeec82c8aa5a69b6e6ed8ada331ccca5846417d42c0d3a7591ac966b2f9b2d25',
    'cdt_odd_mixed_zeta_character_hankel_reduction_20261006.md': 'e6e174a7306d4a9458ff9873d76e5bc40866b258d5d6f760bbf68a28c99ae463',
    'cdt_odd_R0_orbit_nonlinear_jump_hankel_root_review_20261006.md': 'e11abbe660c42704803d1b51b2f59bf48357b6aba76c6c7145c0fc68e1838d6a',
    'cdt_odd_R0_origin_orbit_mod8_arithmetic_independent_review_20261006.md': '615a30cfed0d6696fd36c3b132ae62b23fcdb867e488e58af7273dc995da9338',
    'cdt_odd_R0_origin_orbit_mod8_independent_review_20261006.md': '14766f8cb92e52dd180a5668d2b7d78c0f49963580b60768c3bf9c53cd0edd7c',
    'cdt_odd_R0_nonlinear_projective_invariant_field_independent_review_20261006.md': 'f50624fe3f2fd10bde8aead5ef1687a2f98baa5c0ea6bc88ec185f16cd2f6926',
    'cdt_odd_R0_nonlinear_flag_slopes_independent_review_20261006.md': '5c2215864e27153a0ee37398681062c148b2271d164814eedf7ad8db4916012f',
    'cdt_odd_mixed_zeta_character_hankel_independent_review_20261006.md': 'dfa064d0ddf9361ae48da4fd95e7b8c7816f3d459b4ccb861a679ac53291fe79',
})
current_frozen_pins.update({
    'cdt_odd_mixed_double_pole_arithmetic_cost_20261006.md': '452b9202ab3460f95e1ac5500092146cbe2ba0f9ed1e0a22bf5acb0a291fe985',
    'cdt_odd_mixed_double_pole_analytic_decay_20261006.md': 'c4e8f04f0debe34cf896780424e6ceb256747eaca0d3ed3b9698802757447218',
    'cdt_odd_mixed_double_pole_primitive_lattice_review_20261006.md': '93c9e1705cc63160ce7c212501df79b23b10b249d42acd26a715a538315b8ac8',
    'cdt_odd_double_pole_layout_budget_root_20261006.md': '644f7dbf8e01ec85f938c49435becded48533c88577f712999b6eecb0ae7c3c5',
    'cdt_odd_double_pole_interfaces_root_review_20261006.md': '4245dc1e589cc892e9bd270b5d13bc5246071219f47ccaa57bf744bfd3df317d',
    'cdt_odd_mixed_double_pole_arithmetic_lattice_independent_review_20261006.md': '68a604940cebc4a0bdb403ad0e82b87434768a102463d51eb7f2f90e7ce960b2',
    'cdt_odd_mixed_double_pole_analytic_lattice_arithmetic_independent_review_20261006.md': 'fcb0341687909dcc6070fe88a00d3f888f44e8cc68be701ce613cb6809c2b296',
    'cdt_odd_double_pole_residue_lp_20261006.py': 'bcfdb805967c864ed7e368d29f0690743d894536acc1e24ddd525e420aecad15',
    'cdt_odd_double_pole_residue_lp_20261006.json': 'e8c4b1ee599dad8e13175fbb344dd273ec249d14e2fc0a8b0618c70bfc7f00db',
    'cdt_odd_restored_zero_layout_lp_20261006.py': '17d51f0bc2ab2d2260f2589b61eb90f84fede8e91cfaa5aeea050f08e75ea5cd',
    'cdt_odd_restored_zero_layout_lp_20261006.json': 'e17fa0dfa150914c2f53386f5efefdb52afa36e3e490a57cb042a5b88e1a38c7',
    'cdt_odd_double_pole_budget_certificate_verify_20261006.py': 'b9b4f929f08a74b8e4864ae121038cb5d295c5e05922376f478d391dcd8843e1',
    'cdt_odd_double_pole_budget_certificate_verify_20261006.json': '58827f5454824a236318f8ab91b7a106a2c0b677e05c606126d1a8d6e18d74e3',
})
current_frozen_pins.update({
    'cdt_odd_double_pole_layout_budget_independent_review_20261006.md': '42ead509889102dab52deee02e361a54ab24026d6f07a5a48b7c32f965449fda',
})
current_frozen_pins.update({
    'cdt_odd_restored_zero_equilibrium_energy_20261006.md': '264cc3fce8d8417e04e3aea8963010b0f8804c2014692d4a64827c774454f0e6',
    'cdt_odd_restored_zero_equilibrium_energy_verify_20261006.py': '8aabd288de14fa1b0c72fd72a4b9568ec610b9e22af7ea205de472c8b88e7804',
    'cdt_odd_restored_zero_equilibrium_energy_verify_20261006.json': 'ef3fc4a69593411eb6ae10b680f4b406a22c823c54a5182043e45fd03b339d66',
    'cdt_odd_paired_head_free_integral_lattice_20261006.md': '5b7947c8d26747ca0eb7abac8b3ed5b7cbbe0828170ffe74d7ac51215b1fef5b',
    'cdt_odd_paired_head_free_auxiliary_prime_20261006.md': '4d907340bf9752b3fee94173ecaaddfd81b11cfb5760e8c9954ae4528ce6581b',
    'cdt_odd_paired_head_free_auxiliary_prime_20261006_verify.py': '256f5f32efa8755a6c3c234d25ed2d5395fbf7e45d9402af569c476bb6c94e42',
    'cdt_odd_paired_head_free_auxiliary_prime_20261006_verify.json': 'f8b0f099507d284850fb66ff5236b8e4d5e5d46025ad798c97bca467274ab30a',
    'cdt_odd_paired_head_free_analytic_plucker_root_20261006.md': 'cf341860474546dc0d5a2a630ae73f6bbf50426fa7ee8c100975c6a2b1688e38',
    'cdt_odd_equilibrium_paired_interfaces_root_review_20261006.md': '40e4e7b88ffb68cca834c0f4e7bd77eff03178be86ecdd6538a980ce29e38845',
    'cdt_odd_paired_head_free_analytic_plucker_independent_review_20261006.md': '5b9b5ff67c7aeaea6be24a03a8d9734e15c404aa56dec5c9a577c34ca2ca5d3e',
    'cdt_odd_paired_head_free_integral_lattice_auxiliary_independent_review_20261006.md': 'ae5f49564cb298467cd662e5b7ce636b2bf8125c6c8a40c52e19c64803e842a6',
    'cdt_odd_paired_head_free_auxiliary_prime_independent_review_20261006.md': '96cf18085f73400c9c33801e7c2d8b277245fcd36a30fe5cc22d2c56ad58963f',
    'cdt_odd_restored_zero_equilibrium_energy_independent_review_20261006.md': '7c1213149278d58e6060e6f7f44f1e365f63e2ebae000644df640ab22c6a09b5',
})
current_frozen_pins.update({
    'cdt_odd_paired_primitive_gcd_rate_20261006.md': '77079715fb996f6d2ef9eee370abbbecc1169acb8c14bebfb4515c3b3bf268e2',
    'cdt_odd_paired_primitive_gcd_rate_20261006_verify.py': 'a7bbefb04b33cbaf38937e7595d08fbaca1263da24537147dfd2ea7e55fd67f7',
    'cdt_odd_paired_primitive_gcd_rate_20261006_verify.json': '9ffb2bbacbddb85987ead5b938cafb488cafe798d301f141ffca3e51d9b46f43',
    'cdt_odd_paired_primitive_gcd_rate_independent_review_20261006.md': '9257bbfcf1f52916b460497ed0cb9a14425040382006a4b0b39646f44a718ad2',
    'cdt_odd_paired_plucker_energy_rate_20261006.md': '01c87202a292f9d977f58098bd609e99f9b6aa1b6701e9fff7c036bda7e2515a',
    'cdt_odd_paired_plucker_energy_rate_20261006_verify.py': 'cd43f0cd2965be81f0ad9f077771322f849f4460e2ed5f29d1ea29e29011f129',
    'cdt_odd_paired_plucker_energy_rate_20261006_verify_v2.py': 'ce447f4de73324241725208131be73aea61ef5c5fe44ee044f72fa076b88f3e1',
    'cdt_odd_paired_plucker_energy_rate_20261006_verify_v2.json': '49e3cb42c8c9ddbc8c4ab71b70bee4ebbbf693f4921615330d0a4dbc40b748d8',
    'cdt_odd_paired_all_prime_budget_20261006.md': '55278a0ed68b645fc5cb2f3089563e49c30e608ace9de511cc80d37609b712dc',
    'cdt_odd_paired_all_prime_budget_verify_20261006.py': '01b4970d7d634f2dc5376bce974d3755e7694c1f8a6defec68230aa86f784a95',
    'cdt_odd_paired_all_prime_budget_verify_20261006.json': '7cb512f237d3d29370e164ff3fe69bd319d8685582ef7c6d46d7adf9f738e14b',
    'cdt_odd_paired_all_prime_budget_independent_review_20261006.md': 'a3286743683d751c24251e5a7fb17d85788302758ed6022ce4c8e1ff5f2e9910',
    'cdt_odd_paired_auxiliary_units_structure_20261006.md': 'dcc6d4d670dbcc3960936d3ee1b21a877f73c03e2ba65c479c9d550e0624a8a5',
    'cdt_odd_paired_auxiliary_units_structure_20261006_verify.py': 'b445ebd6b1d52eb1a73fbc4aa003542aa7fb11f9f6ab2551e06fa2ed9a5910c5',
    'cdt_odd_paired_auxiliary_units_structure_20261006_verify.json': 'cc3417ecff851db9aa7a0b37cf38d7e13f114cb8db8e2dab67de643cbdd0e884',
    'cdt_odd_paired_auxiliary_units_structure_independent_review_20261006.md': '9f40ac99af069abca7f20cf05148e7f7b646368836ca948159307ad70fc31638',
    'cdt_odd_paired_rate_units_budget_root_review_20261006.md': 'b587a6b27c076376ad3987006e2ddeb19e38d57e29d922492ebc3464cf13b95a',
})
# Round dual-carry/jet/mirror/symplectic metadata pins
current_frozen_pins.update({'cdt_odd_paired_dual_plucker_carry_rate_20261006.md': '0fb995f69cefcd4e6c92f7ffa42a8e595add4dda9a94951ed27a4693fb127047', 'cdt_odd_paired_dual_plucker_layers_20261006_probe.py': '4b020bc73c49a08a19f49f489bc719bc368d150ce830e3237cd032fd88c9aa1d', 'cdt_odd_paired_dual_plucker_layers_20261006_probe.json': '53b243b65a9a3c7a1a07279b52debabd33bb2c5188ebcf943f3ff82bf60e72d3', 'cdt_odd_paired_dual_plucker_carry_rate_20261006_verify.py': 'ade489f98225ce61a9f58333464ce4d5e91ebfffe149358eb0e4df4b9321c3d5', 'cdt_odd_paired_dual_plucker_carry_rate_20261006_verify_v2.py': '75dda9e61e2a6446e66d1b09502b860294e32e7532e0918f2d346c002e6fa1cf', 'cdt_odd_paired_dual_plucker_carry_rate_20261006_verify_v2.json': '964137827f95314fe269bce3de6a4ddd631f3036b7398ef8507accd04b7bc725', 'cdt_odd_paired_large_prime_jet_rank_20261006.md': '39a0b6f80c4020602aff6dccded6d8da71ce0288b06a4ad86890be3265deb0f5', 'cdt_odd_paired_large_prime_jet_rank_20261006_verify.py': '5c1df7cf287e6865561d22871f8f8ff61a03f1f090a25b9d04b0ad1c1516a17e', 'cdt_odd_paired_large_prime_jet_rank_20261006_verify.json': '190e0aea7a126438037709328576e779b8454c79c815067dc88d6c1b3ac5a99e', 'cdt_odd_paired_mirror_choice_energy_20261006.md': 'cc3821c935474ea1b87011383230b91ac04dcb147c2b09d6ce65e5f899438dd7', 'cdt_odd_paired_mirror_choice_energy_20261006_verify.py': '03fac0d728b448d8168d8d02972e910d82e0194c840365f99c769d31554a3b6a', 'cdt_odd_paired_mirror_choice_energy_20261006_verify.json': 'eb71f6809d98d793f32abca6df7dff199a5d450de73853a5e5bcfcbe72422b9e', 'cdt_odd_paired_auxiliary_pade_symplectic_defect_20261006.md': '452d0271f294b304f3b8bd2a65b343ae5e8b1af128267750e7c9118862066be2', 'cdt_odd_paired_auxiliary_pade_symplectic_defect_20261006_verify.py': '0000ef0f9b98659874603579fc9cf60d1ed5572940f1c150ab007fdd1fa84504', 'cdt_odd_paired_auxiliary_pade_symplectic_defect_20261006_verify.json': 'e751f6c57b27ccf4624bd12b27827bd3edbcfb3e9413d08162238cef2ec7bef7', 'cdt_odd_paired_dual_jet_budget_independent_review_20261006.md': '7fa899348497a05b07eafa45fc75828f999550f0b6bc3d76e74b61c5b0db296a', 'cdt_odd_paired_mirror_choice_energy_independent_review_20261006.md': '759c9b5527b7f2e2998a57197a8adc023cc30c95805c591d3385e3f532a01b91', 'cdt_odd_paired_auxiliary_pade_symplectic_defect_independent_review_20261006.md': 'c4b9df9278f5882666bed21f7f56bb718aa6d8ad5e0425abda3064f6d95b96ef', 'cdt_odd_paired_dual_carry_jet_mirror_root_review_20261006.md': '229167a839321d61076cdc42b835d47dd523dfd57edcd98aae6d517802850e6f'})
# NEW final reviewed CRT/Smith/Jacobi inputs; earlier359 remain untouched.
current_frozen_pins.update({'cdt_odd_paired_residue_crt_integral_model_20261006.md': '3265da7c600ef8c1624f4208448ec35d75e32d71d92d78f4576b2cfdd5cfbd33', 'cdt_odd_paired_residue_crt_integral_model_20261006_verify.py': 'aa4086403985b8b9eab6bec640e538a91f73a819f651a50adaae6bd000ad3f98', 'cdt_odd_paired_residue_crt_integral_model_20261006_verify.json': 'b88deee25e9ee0eef09c64fdd380f48b83062ffc28a2a4213b014ca14e1d640d', 'cdt_odd_paired_residue_crt_integral_model_independent_review_20261006.md': 'ee818081b5a8e4ab746aa52aee80596c40d9f565ae267b20b6e1f83faf4b5983', 'cdt_odd_paired_second_smith_layer_20261006.md': 'd4572c11e52ebdc05ad5338bfe4340e98b696252a5fff6250e1a78b3448a346d', 'cdt_odd_paired_second_smith_layer_20261006_verify.py': '17d76f57b1ae6e8f26ecadc21036a71567759177ca01f2f1fdbccaed00f4e806', 'cdt_odd_paired_second_smith_layer_20261006_verify.json': '516d84723f0a827dfafea94eb28db7917ffd1b2a45157b9b7adbdc154acff735', 'cdt_odd_paired_smith_credit_cap_transfer_20261006.md': '8b7368457b4e147e16a3de12e62db330ebaccc3b7da0faaa6e725842885d37b0', 'cdt_odd_paired_smith_credit_cap_transfer_20261006_verify.py': '378962de4c7f87851dc2e942318277b92d66b24814af00db43f9df009331711d', 'cdt_odd_paired_smith_credit_cap_transfer_20261006_verify.json': 'cf308c972e1279686684a641acc58a4a5c1d3d8382bce14c4ae5990c5d175e7f', 'cdt_odd_paired_auxiliary_boundary_jacobi_krylov_20261006.md': '09b9e74683f4767c2a69eb5a7d67893fda1c6d6bb738d2b245f8f692fc20d17f', 'cdt_odd_paired_auxiliary_boundary_jacobi_krylov_20261006_verify.py': 'ef2dd914c860485b76a29ce8566a2385c4e4bc12d285da72c6ad4a29ef1ab8fa', 'cdt_odd_paired_auxiliary_boundary_jacobi_krylov_20261006_verify.json': '7ece9d110eb1f2580ccd549cf5250c5b3172f774e3af9501e3a63873be87a180', 'cdt_odd_paired_auxiliary_boundary_jacobi_krylov_independent_review_20261006.md': 'd796d65f661146cf42b430587500a1ad18bef0289f79b32ff3eb8ff8edf27072', 'cdt_odd_paired_crt_smith_jacobi_root_review_20261006.md': '21bf0f92daaebd6a912a84e8f923d12690258474216611fa7f43c84d8ec2033c'})
current_frozen_pins.update({'cdt_odd_paired_smith_credit_cap_transfer_independent_review_20261006.md': '4265626dd0887dc141c3250903b8a9d039f5432a102c9ceef23bc977c5ae9536'})
# NEW final reviewed support/direct-Gram/weighted/modified-target mathematics.
current_frozen_pins.update({'cdt_odd_paired_support_correlated_budget_20261006.md': '150bb58d8d5a0463bb8747bf1e9e8a549727973b89d133b620b5d3535fd1601e', 'cdt_odd_paired_support_correlated_budget_20261006_verify.py': 'cd659ad52bad2d829bcbe9ec0c54812f3c238b00559f8e4aef6a4df337e31153', 'cdt_odd_paired_support_correlated_budget_20261006_verify.json': '6db2c221a8e19496eda0005ce1ac4918d53dfb4e103f46d57f54fee51401f2f0', 'cdt_odd_paired_actual_local_gram_layers_20261006.md': '2856a47ab3aa407f1eb7477a57e1e44bd010a7dd95b8cb055a603b68ea091094', 'cdt_odd_paired_actual_local_gram_layers_20261006_verify.py': 'e9a512a8bb9f40b6c84144eeeaf52eb9761a0ef0699adc4e82af07d8c0c1ebf9', 'cdt_odd_paired_actual_local_gram_layers_20261006_verify.json': '0fd35bb97e6f16a6a7ac273e0bd8baba1b7afc8f91f321c8a038416d4fdd900e', 'cdt_odd_paired_weighted_jet_support_budget_20261006.md': 'b9535b241ef67af5d5ce82aaa8bd5073e844dd5a9b5701f12669b1cc9a5211cb', 'cdt_odd_paired_weighted_jet_support_budget_20261006_verify.py': '36112ffcb950479e89a1744ee35721770f8216cd96b7352d7c9b785ad5e40932', 'cdt_odd_paired_weighted_jet_support_budget_20261006_verify.json': 'bb3ceac4bb22ac030fbf8ed43337738b70b0af3fdf7f687147862e5f1b7a4eba', 'cdt_odd_paired_jacobi_modified_target_normality_20261006.md': 'c4dcee183239be55ab6c4e06d4b1abb1979657838f02a5c64104c45cc1fed9c4', 'cdt_odd_paired_jacobi_modified_target_normality_20261006_verify.py': '4f525b33ca7664912192daab4628db39a992ed9f3bea1df753bc6e3f253aa69b', 'cdt_odd_paired_jacobi_modified_target_normality_20261006_verify.json': 'b9f5285e3440101fa326a00c0303259262202aa428073374ec00727fa1d31a84', 'cdt_odd_paired_support_gram_modified_target_root_review_20261006.md': 'a8493b979e4a3f6ea9dcf2e90819cb688c405461a724435ec47a9af6ea46d3c9', 'cdt_odd_paired_weighted_jet_support_budget_independent_review_20261006.md': '5278b427215c223f5e545d93d24cc22cec5151f55227212a572337acae2a4faa', 'cdt_odd_paired_direct_gram_support_independent_review_20261006.md': '80c2095ba8fa2fbc7cf21c83335240c5666e573154644036a0490763b3a9c331', 'cdt_odd_paired_jacobi_modified_target_normality_independent_review_20261006.md': 'e637161d8c60bad3f7795b559a0330b5c764be8d312a33179edbfdd739153e5b'})
# Latest round; these checks only read immutable files and saved outputs.
current_frozen_pins.update({
    'cdt_odd_paired_actual_unit_sector_rank_20261006.md': 'e4830013ad948599c4e1bb76113aeed3a8b6df23b32a9d575052cd97d7f6fac8',
    'cdt_odd_paired_actual_unit_sector_rank_20261006_verify.py': 'e64add398faeae06855192fcc46a352702f156b191f3668db9dc83e3a6c82b1c',
    'cdt_odd_paired_actual_unit_sector_rank_20261006_verify.json': 'a0f74c85d2da7343eb1422091bf8670799eff675ad4f7f158976d70ce62bb6d5',
    'cdt_odd_paired_weighted_jet_global_optimization_20261006.md': '1b7923801d7ff734d278163350d661516abf78fde0687976c4db1d6ef4c6f34f',
    'cdt_odd_paired_weighted_jet_global_optimization_20261006_verify.py': '1e8c6a6000a70a8484e69536da6e09946bf65000545a16d58a053de241ac54d3',
    'cdt_odd_paired_weighted_jet_global_optimization_20261006_verify.json': '5bb704e25707379253bb7733d86c44a354c917bc4c12b96fcd34dfda70bf2863',
    'cdt_odd_paired_single_bordered_nonzero_gate_20261006.md': 'a60d8116c88581028669d9a91aaaf1b848761fcfc4a37b089ca6e5b490b590f8',
    'cdt_odd_paired_single_bordered_nonzero_gate_20261006_verify.py': '84e3c06bb135ec57235880fa1490afe4a9c17e07fef62541219ce99e329e1cb3',
    'cdt_odd_paired_single_bordered_nonzero_gate_20261006_verify.json': '0273fdab538337a3a617aaed658db0e9a2e6559c91de65fc20448942a493b3ba',
    'cdt_odd_paired_fixed_middle_gosper_reduction_20261006.md': 'f988d6629b01188f175fabcfa0e87fc58d51d1bf482fda8196d1fd67f2bad4c7',
    'cdt_odd_paired_fixed_middle_gosper_reduction_20261006_verify.py': '4b6dce00c79c0d26d89a418af05966d8f8a7ada32b00ce636c9de20b6576b012',
    'cdt_odd_paired_fixed_middle_gosper_reduction_20261006_verify.json': '05907586c7113e74a9e47960de7561f0eb2964a5d56973cb51fd4e333e348b28',
    'cdt_odd_paired_single_bordered_nonzero_gate_independent_review_20261006.md': 'cdd45a63d666383c0953af77a91578996a01ddb761096a131f6383600df6a7a7',
    'cdt_odd_paired_unit_sector_flow_independent_review_20261006.md': '80eadb93166628891f2e659cfdb9cccc15c72b18072f9d8bc1c6b7f630ec5eaa',
    'cdt_odd_paired_rank_flow_gosper_root_review_20261006.md': '3642fa37a6615566f6cb5dee872fb2252d92887714e664d1d6bb7fa4cb7937e5',
    'cdt_odd_paired_fixed_middle_gosper_reduction_independent_review_20261006.md': '6303175981178497e34383ba0dc737f0ade3d3bda421eb9a968b6763891a37a6',
})
# Completed supported/Racah/depth4 round: immutable proofs, results and execution guard.
current_frozen_pins.update({
    "cdt_odd_paired_selected_jet_primitive_support_20261006.md": "35ed9d8e9b3f1f5ea70c4e742d1e26c262d6d529823987bdc0478128fdd35880",
    "cdt_odd_paired_selected_jet_primitive_support_20261006_verify.py": "1aec5fd218fdb9ba920eb579b5d1d09318c3828c0cb6d30ab9b632caafb79b2e",
    "cdt_odd_paired_selected_jet_primitive_support_20261006_verify.json": "07d7dd36f8b0c094676532ba8b86d36e7c7a882b2b11b37b1e18897c4d1f57bc",
    "cdt_odd_paired_supported_weighted_dual_transfer_20261006.md": "3a4b58d6d0fbad83e13268e4b30d73030caf8461c99a4db0acb5681ba1625334",
    "cdt_odd_paired_supported_weighted_dual_transfer_20261006_verify.py": "92b737b19375e973c97b67830477b10313b365f617df6dc5e0f193e74bd0aa94",
    "cdt_odd_paired_supported_weighted_dual_transfer_20261006_verify.json": "a37ce3e552a6ded9efaa48f07ca268ec207000d4a165cc4e072ba52dc31f1694",
    "cdt_odd_paired_value_gram_depth4_nonzero_20261006.md": "57f9aa8cb6335556399cb624316401f419b3174d8137ea3138e5ae2a51877ec7",
    "cdt_odd_paired_value_gram_depth4_nonzero_20261006_verify.py": "bc3a54157f1d36c892ecbbf1f4209737244ecdfe5533bec49da95e52b4e24785",
    "cdt_odd_paired_value_gram_depth4_nonzero_20261006_verify.json": "f50b9b63458365a81381d0ed4b6ef12c3a627a9e7782da815820a2764d348908",
    "cdt_odd_paired_fixed_middle_racah_border_20261006.md": "2e04fe760174e006b697de7e8756cce85734f695010ac43c0f74e0fbc20e2f24",
    "cdt_odd_paired_fixed_middle_racah_border_20261006_verify.py": "f36a0ca4740926620306db99be3c4e07bc04c97d52ef4b67b498de410518395d",
    "cdt_odd_paired_fixed_middle_racah_border_20261006_verify.json": "c99024507adc6419cde98bef171c63c44aa4090e30075bbe4c13edb3b03f5a62",
    "cdt_odd_paired_fixed_middle_racah_border_20261006_verify.guard.json": "25c3d5c6a77213f8a7f8dbf835feb32bee75b474af4b126d77f8832f6dd9194c",
    "cdt_odd_paired_value_gram_depth4_nonzero_independent_review_20261006.md": "43ad1118f51a1ddb8545103d4c19b245030368d055e33278dc3e463185d8271b",
    "cdt_odd_paired_fixed_middle_racah_border_independent_review_20261006.md": "763e586e86ec1d967f9540e0d142743db43ca55c7eabfab8bc875df2a9c92e89",
    "cdt_odd_paired_supported_jet_transfer_independent_review_20261006.md": "5e2201638eedae6fdb47600f6cd2cf8defcf60cf34061c01c100e0778e43af5d",
    "cdt_odd_paired_supported_racah_depth4_root_review_20261006.md": "b720e79b859ddb3b5f16b908fedd794e7ca378c9c2c598bbeaf5dd6fc8c13828"
})
current_frozen = []
for name, expected in current_frozen_pins.items():
    actual = sha(local(name))
    assert actual == expected, name
    current_frozen.append({'file': name, 'sha256': actual, 'unchanged': True})

stems = [
    'cdt_odd_period_trigger_20261005',
    'cdt_odd_level12_model_20261005',
    'cdt_odd_holonomy_budget_20261005',
    'cdt_odd_character_targets_20261005',
    'cdt_odd_mixed_filtration_20261005',
    'cdt_odd_algebraic_helpers_20261005',
    'cdt_odd_congruence_background_20261005',
    'cdt_odd_conjugate_projection_20261005',
    'cdt_odd_low_period_coupling_20261005',
    'cdt_odd_tensor_helpers_20261005',
    'cdt_odd_level20_model_20261006',
    'cdt_odd_level20_arithmetic_20261006',
    'cdt_odd_level20_leaf_20261006',
    'cdt_odd_level20_convexity_20261006',
    'cdt_odd_low_cost_polylog_20261006',
    'cdt_odd_level20_hasse_20261006',
    'cdt_odd_level20_frobenius_20261006',
    'cdt_odd_level20_third_layer_20261006',
    'cdt_odd_level20_square_lift_20261006',
    'cdt_odd_level20_balanced_smith_bridge_20261006',
    'cdt_odd_level20_universal_s2_20261006',
    'cdt_odd_level20_large_prime_net_20261006',
    'cdt_odd_level20_squarelift_modp3_obstruction_20261006',
    'cdt_odd_level20_post_smith_budget_20261006',
    'cdt_odd_level20_integrated_tensor_bridge_20261006',
    'cdt_odd_level20_target_integral_20261006',
    'cdt_odd_level20_cartier_kernel_20261006',
    'cdt_odd_level20_cartier_cohomology_20261006',
    'cdt_odd_level20_cartier_source_elimination_20261006',
    'cdt_odd_level20_hecke_space_20261006',
    'cdt_odd_level20_cartier_rank19_budget_20261006',
    'cdt_odd_level20_cartier_native_s1_budget_20261006',
    'cdt_odd_level20_cartier_rational_primitive_20261006',
    'cdt_odd_level20_cartier_background_slow_packet_20261006',
    'cdt_odd_candidates_5_8_12_20261006',
    'cdt_odd_level20_cartier_slow_intersection_20261006',
    'cdt_odd_level20_cartier_p13_polynomial_20261006',
    'cdt_odd_level20_cartier_poly_k1_20261006',
    'cdt_odd_level8_mixed_embedding_20261006',
    'cdt_odd_level8_mixed_period_review_20261006',
    'cdt_odd_level8_three_source_projection_20261006',
    'cdt_odd_level12_source_period_20261006',
    'cdt_odd_level12_paired_coordinate_20261006',
    'cdt_odd_level12_joint_trigger_20261006',
    'cdt_odd_level12_full_leaf_20261006',
    'cdt_odd_level12_budget_20261006',
    'cdt_odd_level12_cheap_log_packet_20261006',
    'cdt_odd_level12_cheap_log_transport_20261006',
    'cdt_odd_level12_hecke_radius_20261006',
    'cdt_odd_level12_augmented_radius_20261006',
    'cdt_odd_level12_signed_cocycle_20261006',
    'cdt_odd_level12_gamma_cocycle_20261006',
    'cdt_odd_level12_schreier_presentation_20261006',
    'cdt_odd_level12_generator_cocycle_20261006',
    'cdt_odd_level12_stabilizer_structure_20261006',
    'cdt_odd_level12_stabilizer_boundary_20261006',
    'cdt_odd_level12_stabilizer_mixed_cusp_pair_20261006',
    'cdt_odd_level12_stabilizer_parabolic_malnormal_20261006',
    'cdt_odd_level12_zero_period_corrector_family_20261006',
    'cdt_odd_classical_derivative_projection_20261006',
    'cdt_odd_level12_eisenstein_extension_20261006',
    'cdt_odd_classical_spin_pullback_20261006',
    'cdt_odd_classical_spin_monodromy_20261006',
    'cdt_odd_classical_zeta7_forcing_20261006',
    'cdt_odd_level12_corrector_multireflection_20261006',
    'cdt_odd_classical_zeta7_full_rank_20261006',
    'cdt_odd_level12_cuspidal_corrector_window_20261006',
    'cdt_odd_classical_conifold_calibration_20261006',
    'cdt_odd_classical_frobenius_smith_20261006',
    'cdt_odd_level12_manin_period_interface_20261006',
    'cdt_odd_classical_M4_bilateral_reduction_20261006',
    'cdt_odd_quarter_shift_smith_20261006',
    'cdt_odd_level12_trivial_cusp_period_20261006',
    'cdt_odd_quarter_product_mixed_packet_20261006',
    'cdt_odd_conifold_arithmetic_center_20261006',
    'cdt_odd_R0_actual_vanishing_orbit_lattice_20261006',
    'cdt_odd_R0_conifold_effective_denominator_20261006',
]
# This certificate uses source_sha256 for a frozen input certificate,
# and script_sha256 for its own producer. Bind each pin to its declared role.
certificate_source_paths = {
    'cdt_odd_level20_large_prime_net_20261006':
        'cdt_odd_level20_hasse_20261006_verify.json',
}
certificate_suffixes = {
    'cdt_odd_level20_hecke_space_20261006': ('.py', '.json'),
}
certificate_path_overrides = {
    'cdt_odd_R0_conifold_effective_denominator_20261006':
        ('cdt_odd_R0_conifold_effective_denominator_20261006_symbolic_verify.py',
         'cdt_odd_R0_conifold_effective_denominator_20261006_symbolic_verify.json'),
    'cdt_odd_level20_cartier_p13_polynomial_20261006':
        ('cdt_odd_level20_cartier_p13_20261006_verify.py',
         'cdt_odd_level20_cartier_p13_20261006_verify.json'),
    'cdt_odd_level12_joint_trigger_20261006':
        ('cdt_odd_level12_source_family_20261006_verify.py',
         'cdt_odd_level12_source_family_20261006_verify.json'),
}
certificate_frozen_paths = {
    'cdt_odd_R0_conifold_effective_denominator_20261006': {
        'author_new_data_sha256': 'cdt_odd_R0_conifold_effective_denominator_20261006_probe.json',
    },
    'cdt_odd_level20_cartier_p13_polynomial_20261006': {
        'frozen_T3_data_sha256': 'cdt_odd_level20_hecke_space_20261006.json',
    },
    'cdt_odd_level12_generator_cocycle_20261006': {
        'input_json_sha256': 'cdt_odd_level12_schreier_presentation_20261006_verify.json',
    },
    'cdt_odd_level12_stabilizer_boundary_20261006': {
        'input_json_sha256': 'cdt_odd_level12_generator_cocycle_20261006_verify.json',
    },
    'cdt_odd_level12_corrector_multireflection_20261006': {
        'input_sha256': 'cdt_odd_level12_generator_cocycle_20261006_verify.json',
    },
}
reports = []
for stem in stems:
    report = local(stem + '.md')
    script_suffix, cert_suffix = certificate_suffixes.get(stem, ('_verify.py', '_verify.json'))
    script_name, cert_name = certificate_path_overrides.get(
        stem, (stem + script_suffix, stem + cert_suffix))
    script = local(script_name)
    cert = local(cert_name)
    data = json.loads(cert.read_text(encoding='utf-8'))
    pins = []
    for key, path in [('source_sha256', script), ('script_sha256', script),
                      ('producer_sha256', script),
                      ('report_sha256', report)]:
        if key in data and data[key] is not None:
            if key == 'source_sha256' and stem in certificate_source_paths:
                path = local(certificate_source_paths[stem])
            assert data[key] == sha(path), (stem, key)
            pins.append(key)
    fixed_dict_check_counts = {
        'cdt_odd_level12_manin_period_interface_20261006': 40,
        'cdt_odd_level12_trivial_cusp_period_20261006': 28,
    }
    if stem in fixed_dict_check_counts:
        assert isinstance(data['checks'], dict) and len(data['checks']) == data['passed'] == fixed_dict_check_counts[stem]
        assert all(v is True for v in data['checks'].values())
    labels = data.get('checks') if isinstance(data.get('checks'), list) else data.get('check_labels')
    if isinstance(labels, list):
        for item in labels:
            if isinstance(item, dict) and 'passed' in item:
                assert item['passed'] is True, (stem, item)
    if isinstance(data.get('failed'), int):
        assert data['failed'] == 0, (stem, 'failed checks')
    if isinstance(data.get('passed'), int) and not isinstance(data['passed'], bool) and isinstance(labels, list):
        assert data['passed'] == len(labels), (stem, 'passed count')
    for key, name in certificate_frozen_paths.get(stem, {}).items():
        assert data[key] == sha(local(name)), (stem, key)
        pins.append(key)
    # This new certificate names two frozen Markdown proof inputs explicitly.
    # Check their declared roles, without importing or executing any producer.
    for name, expected in data.get('input_pins', {}).items():
        assert expected == sha(local(name)), (stem, 'input_pins', name)
        pins.append('input_pins:' + name)
    if stem in {'cdt_odd_level12_stabilizer_parabolic_malnormal_20261006',
                'cdt_odd_classical_zeta7_forcing_20261006'}:
        for name, expected in data.get('pins', {}).items():
            assert expected == sha(local(name)), (stem, 'pins', name)
            pins.append('pins:' + name)
    for name, expected in data.get('source_pdf_sha256', {}).items():
        assert expected == sha(local(name, ROOT / 'literature')), (stem, 'source PDF', name)
        pins.append('source_pdf_sha256:' + name)
    finite_count = len(labels) if isinstance(labels, list) else data.get('checks_passed')
    if stem == 'cdt_odd_conifold_arithmetic_center_20261006':
        assert data['status'] == 'passed'
        assert len(data['identities']) == 6
        assert data['old_or_peer_producer_executed'] is False
        assert data['numeric_irrationality_proved'] is False
        finite_count = None  # All-symbolic-n identities, not finite samples.
    if stem in fixed_dict_check_counts:
        finite_count = len(data['checks'])
    if stem == 'cdt_odd_quarter_shift_smith_20261006':
        assert finite_count == data['finite_check_count'] == 24
    if finite_count is None and isinstance(data.get('fixed_results'), list):
        finite_count = len(data['fixed_results'])
    if isinstance(data.get('checks_passed'), int) and isinstance(labels, list):
        assert data['checks_passed'] == len(labels), (stem, 'check count')
    if isinstance(data.get('check_count'), int) and isinstance(labels, list):
        assert data['check_count'] == len(labels), (stem, 'declared check count')
    if 'all_passed' in data:
        assert data['all_passed'] is True, (stem, 'all_passed')
    if data.get('input_certificate') and data.get('input_sha256'):
        input_path = local(Path(data['input_certificate']).name)
        assert sha(input_path) == data['input_sha256'], (stem, 'input certificate')
        pins.append('input_sha256')
    reports.append({'report': report.name, 'report_sha256': sha(report),
                    'script': script.name, 'script_sha256': sha(script),
                    'certificate': cert.name, 'certificate_sha256': sha(cert),
                    'certificate_status': data.get('status'),
                    'certificate_pins_checked': pins,
                    'finite_check_count': finite_count,
                    'symbolic_identity_family_count': len(data['identities'])
                        if stem == 'cdt_odd_conifold_arithmetic_center_20261006' else None})

# NEW own finite-prefix data is provenance only; never execute its producer.
dyadic_probe_report = local('cdt_odd_R0_conifold_effective_denominator_20261006.md')
dyadic_probe_script = local('cdt_odd_R0_conifold_effective_denominator_20261006_probe.py')
dyadic_probe_cert = local('cdt_odd_R0_conifold_effective_denominator_20261006_probe.json')
dyadic_probe_data = json.loads(dyadic_probe_cert.read_text(encoding='utf-8'))
assert dyadic_probe_data['status'] == 'finite_exact_recurrence_data_only'
assert dyadic_probe_data['prefix_degree'] == 180
assert dyadic_probe_data['old_or_peer_math_producers_executed_or_imported'] == 0
reports.append({'report': dyadic_probe_report.name,
                'report_sha256': sha(dyadic_probe_report),
                'script': dyadic_probe_script.name,
                'script_sha256': sha(dyadic_probe_script),
                'certificate': dyadic_probe_cert.name,
                'certificate_sha256': sha(dyadic_probe_cert),
                'finite_check_count': None,
                'finite_prefix_degree': 180,
                'scope': dyadic_probe_data['scope']})

probe_report = local('cdt_odd_level20_large_prime_smith_probe_20261006.md')
probe_script = local('cdt_odd_level20_large_prime_smith_probe_20261006.py')
probe_cert = local('cdt_odd_level20_large_prime_smith_probe_20261006.json')
probe_data = json.loads(probe_cert.read_text(encoding='utf-8'))
assert probe_data['source_sha256'] == sha(probe_script)
assert probe_data['checks_passed'] == len(probe_data['check_labels']) == 38
assert len(probe_data['samples']) == 4
square_probe = {'report': probe_report.name, 'report_sha256': sha(probe_report),
                'script': probe_script.name, 'script_sha256': sha(probe_script),
                'certificate': probe_cert.name, 'certificate_sha256': sha(probe_cert),
                'finite_check_count': 38, 'scope': probe_data['scope']}

new_proof_files = [
    'cdt_odd_background_progress_20261006.md',
    'cdt_odd_level20_hasse_global_20261006.md',
    'cdt_odd_level20_review_20261006.md',
    'cdt_odd_level20_hasse_review_20261006.md',
    'cdt_odd_level20_hasse_smith_bridge_20261006.md',
    'cdt_odd_level20_hasse_smith_audit_20261006.md',
    'cdt_odd_level20_frobenius_review_20261006.md',
    'cdt_odd_level20_third_layer_review_20261006.md',
    'cdt_odd_level20_squarelift_review_20261006.md',
    'cdt_odd_level20_fixed_source_ceiling_20261006.md',
    'cdt_odd_level20_balanced_smith_bridge_20261006.md',
    'cdt_odd_level20_large_prime_smith_probe_20261006.md',
    'cdt_odd_level20_cartier_primary_input_20261006.md',
    'cdt_odd_level20_cartier_primitive_leaf_20261006.md',
    'cdt_odd_level20_cartier_packet_matrix_20261006.md',
    'cdt_odd_level20_cartier_native_rank_20261006.md',
    'cdt_odd_level20_cartier_packet_s2_20261006.md',
    'cdt_odd_level20_cartier_large_prime_baseline_20261006.md',
    'cdt_odd_level20_cartier_mixed_bockstein_20261006.md',
    'cdt_odd_level20_cartier_mixed_source_budget_20261006.md',
    'cdt_odd_level12_source_denominators_20261006.md',
    'cdt_odd_level12_source_period_finite_review_20261006.md',
    'cdt_odd_level12_character_tensor_20261006.md',
    'cdt_odd_level12_joint_full_model_20261006.md',
    'cdt_odd_level12_mixed_log_smith_20261006.md',
    'cdt_odd_level12_affine_galois_20261006.md',
    'cdt_odd_level12_affine_galois_review_20261006.md',
    'cdt_odd_level12_vector_leaf_numerator_20261006.md',
    'cdt_odd_level12_nongauged_rank_20261006.md',
    'cdt_odd_level12_stabilizer_timelike_conjugates_20261006.md',
    'cdt_odd_level12_stabilizer_signed_powers_20261006.md',
    'cdt_odd_level12_stabilizer_full_timelike_conjugates_20261006.md',
    'cdt_odd_level12_hodge_bundle_evaluation_20261006.md',
    'cdt_odd_level12_corrector_green_budget_20261006.md',
    'cdt_odd_classical_zeta7_forcing_spin_20261006.md',
    'cdt_odd_spin_corrector_review_20261006.md',
    'cdt_odd_connection_moments_20261006.md',
    'cdt_odd_classical_lambda_leaf_arithmetic_20261006.md',
    'cdt_odd_rank_connection_cusp_review_20261006.md',
]
new_proof_files += ['cdt_odd_bailey_M1_period_20261006.md', 'cdt_odd_calibrated_period_smith_review_20261006.md']
new_proof_files += [
    'cdt_odd_quarter_shift_full_model_20261006.md',
    'cdt_odd_quarter_shift_independent_review_20261006.md',
    'cdt_odd_quarter_shift_cost_independent_review_20261006.md',
    'cdt_odd_R0_kummer_period_interface_20261006.md',
    'cdt_odd_R0_kummer_independent_review_20261006.md',
    'cdt_odd_ehmm_special_fiber_targets_20261006.md',
    'cdt_odd_quarter_kummer_three_source_review_20261006.md',
]
new_proof_files += [
    'cdt_odd_complete_F_high_filtration_20261006.md',
    'cdt_odd_complete_F_cost_bridge_20261006.md',
    'cdt_odd_complete_F_cost_independent_review_20261006.md',
    'cdt_odd_complete_F_R0_independent_review_20261006.md',
    'cdt_odd_complementary_quarter_period_product_20261006.md',
    'cdt_odd_quarter_product_rank19_interface_20261006.md',
    'cdt_odd_rational_conifold_projection_20261006.md',
    'cdt_odd_R0_relative_cycle_mirror_20261006.md',
    'cdt_odd_R0_relative_cycle_independent_review_20261006.md',
    'cdt_odd_integral_cycle_full_F_product_review_20261006.md',
]
new_proof_files += [
    'cdt_odd_quarter_product_actual_rank19_20261006.md',
    'cdt_odd_quarter_product_mixed_packet_20261006.md',
    'cdt_odd_conifold_arithmetic_center_20261006.md',
    'cdt_odd_R0_toric_completion_20261006.md',
    'cdt_odd_conifold_arithmetic_center_independent_review_20261006.md',
    'cdt_odd_quarter_actual_rank19_independent_review_20261006.md',
    'cdt_odd_quarter_actual_rank_mixed_independent_review_20261006.md',
    'cdt_odd_R0_toric_completion_independent_review_20261006.md',
    'cdt_odd_toric_completion_conifold_center_root_review_20261006.md',
    'cdt_odd_R0_toric_completion_uniqueness_20261006.md',
    'cdt_odd_R0_boundary_completion_uniqueness_independent_20261006.md',
    'cdt_odd_R0_toric_uniqueness_author_independent_review_20261006.md',
]
new_proof_files += [
    'cdt_odd_R0_klm_current_interface_20261006.md',
    'cdt_odd_R0_regulator_derivative_20261006.md',
    'cdt_odd_R0_Yukawa_scalar_interface_20261006.md',
    'cdt_odd_R0_positive_cut_period_comparison_20261006.md',
    'cdt_odd_R0_regulator_yukawa_root_review_20261006.md',
    'cdt_odd_R0_positive_cut_period_comparison_independent_review_20261006.md',
    'cdt_odd_R0_Yukawa_independent_review_20261006.md',
]
new_proof_files += [
    'cdt_odd_R0_vanishing_regulator_normalization_20261006.md',
    'cdt_odd_R0_compact_positive_cut_class_20261006.md',
    'cdt_odd_R0_boundary_membrane_comparison_20261006.md',
    'cdt_odd_R0_conifold_actual_arithmetic_hypotheses_20261006.md',
    'cdt_odd_R0_vanishing_regulator_normalization_independent_review_20261006.md',
    'cdt_odd_R0_boundary_membrane_comparison_independent_review_20261006.md',
    'cdt_odd_R0_conifold_actual_arithmetic_hypotheses_independent_review_20261006.md',
    'cdt_odd_R0_current_cycle_arithmetic_root_review_20261006.md',
]
new_proof_files += [
    'cdt_odd_R0_noncompact_Tate_boundary_period_20261006.md',
    'cdt_odd_R0_positive_cut_boundary_flux_20261006.md',
    'cdt_odd_R0_real_Betti_normalization_20261006.md',
    'cdt_odd_R0_endpoint_sensitive_exterior_packet_20261006.md',
    'cdt_odd_R0_noncompact_Tate_boundary_period_independent_review_20261006.md',
    'cdt_odd_R0_positive_cut_boundary_flux_independent_review_20261006.md',
    'cdt_odd_R0_endpoint_sensitive_exterior_packet_independent_review_20261006.md',
    'cdt_odd_R0_boundary_real_exterior_root_review_20261006.md',
]
new_proof_files += [
    'cdt_odd_R0_conifold_effective_denominator_20261006.md',
    'cdt_odd_R0_actual_vanishing_orbit_lattice_20261006.md',
    'cdt_odd_R0_regulator_Betti_extension_flag_20261006.md',
    'cdt_odd_R0_endpoint_flag_holonomy_interface_20261006.md',
    'cdt_odd_R0_toric_odd_prime_smooth_model_20261006.md',
    'cdt_odd_R0_all_odd_generic_radius_arithmetic_interface_20261006.md',
    'cdt_odd_R0_actual_vanishing_orbit_lattice_independent_review_20261006.md',
    'cdt_odd_R0_Betti_denominator_independent_review_20261006.md',
    'cdt_odd_R0_actual_Betti_integer_lattices_independent_review_20261006.md',
    'cdt_odd_R0_endpoint_flag_holonomy_independent_review_20261006.md',
    'cdt_odd_R0_integral_flag_denominator_holonomy_root_review_20261006.md',
    'cdt_odd_R0_all_odd_radius_independent_review_20261006.md',
    'cdt_odd_R0_all_odd_generic_radius_independent_review_20261006.md',
    'cdt_odd_R0_dyadic_number_field_scale_supplement_20261006.md',
    'cdt_odd_R0_dyadic_number_field_scale_independent_review_20261006.md',
]
new_proof_files += [
    'cdt_odd_R0_origin_orbit_mod8_obstruction_20261006.md',
    'cdt_odd_R0_nonlinear_projective_invariant_field_20261006.md',
    'cdt_odd_R0_logarithmic_flag_slopes_reduction_20261006.md',
    'cdt_odd_mixed_zeta_character_hankel_reduction_20261006.md',
    'cdt_odd_R0_orbit_nonlinear_jump_hankel_root_review_20261006.md',
    'cdt_odd_R0_origin_orbit_mod8_arithmetic_independent_review_20261006.md',
    'cdt_odd_R0_origin_orbit_mod8_independent_review_20261006.md',
    'cdt_odd_R0_nonlinear_projective_invariant_field_independent_review_20261006.md',
    'cdt_odd_R0_nonlinear_flag_slopes_independent_review_20261006.md',
    'cdt_odd_mixed_zeta_character_hankel_independent_review_20261006.md',
]
new_proof_files += [
    'cdt_odd_mixed_double_pole_arithmetic_cost_20261006.md',
    'cdt_odd_mixed_double_pole_analytic_decay_20261006.md',
    'cdt_odd_mixed_double_pole_primitive_lattice_review_20261006.md',
    'cdt_odd_double_pole_layout_budget_root_20261006.md',
    'cdt_odd_double_pole_interfaces_root_review_20261006.md',
    'cdt_odd_mixed_double_pole_arithmetic_lattice_independent_review_20261006.md',
    'cdt_odd_mixed_double_pole_analytic_lattice_arithmetic_independent_review_20261006.md',
]
new_proof_files += ['cdt_odd_double_pole_layout_budget_independent_review_20261006.md']
for budget_stem in ['cdt_odd_double_pole_residue_lp_20261006',
                    'cdt_odd_restored_zero_layout_lp_20261006',
                    'cdt_odd_double_pole_budget_certificate_verify_20261006']:
    budget_script = local(budget_stem + '.py')
    budget_cert = local(budget_stem + '.json')
    budget_data = json.loads(budget_cert.read_text(encoding='utf-8'))
    assert budget_data['new_producer_execution_ordinal'] == 1
    assert budget_data['old_or_peer_producer_execution_import_rerun'] == 0
    budget_report = local('cdt_odd_double_pole_layout_budget_root_20261006.md')
    reports.append({'report': budget_report.name, 'report_sha256': sha(budget_report),
                    'script': budget_script.name, 'script_sha256': sha(budget_script),
                    'certificate': budget_cert.name, 'certificate_sha256': sha(budget_cert),
                    'certificate_status': budget_data['status'],
                    'certificate_pins_checked': [], 'finite_check_count': None,
                    'certificate_scope': budget_data['scope'],
                    'new_this_round_first_execution_only': True})
new_proof_files += [
    'cdt_odd_restored_zero_equilibrium_energy_20261006.md',
    'cdt_odd_restored_zero_equilibrium_energy_independent_review_20261006.md',
    'cdt_odd_paired_head_free_integral_lattice_20261006.md',
    'cdt_odd_paired_head_free_auxiliary_prime_20261006.md',
    'cdt_odd_paired_head_free_analytic_plucker_root_20261006.md',
    'cdt_odd_equilibrium_paired_interfaces_root_review_20261006.md',
    'cdt_odd_paired_head_free_analytic_plucker_independent_review_20261006.md',
    'cdt_odd_paired_head_free_integral_lattice_auxiliary_independent_review_20261006.md',
    'cdt_odd_paired_head_free_auxiliary_prime_independent_review_20261006.md',
]
# Metadata only: neither new peer mathematical producer is imported or run.
equilibrium_script = local('cdt_odd_restored_zero_equilibrium_energy_verify_20261006.py')
equilibrium_cert = local('cdt_odd_restored_zero_equilibrium_energy_verify_20261006.json')
equilibrium_data = json.loads(equilibrium_cert.read_text(encoding='utf-8'))
assert equilibrium_data['status'] == 'PASS'
assert equilibrium_data['producer_execution'] == 'first execution only'
assert equilibrium_data['producer_sha256'] == sha(equilibrium_script)
assert equilibrium_data['exact_checks'] == 18
equilibrium_report = local('cdt_odd_restored_zero_equilibrium_energy_20261006.md')
reports.append({'report': equilibrium_report.name, 'report_sha256': sha(equilibrium_report),
                'script': equilibrium_script.name, 'script_sha256': sha(equilibrium_script),
                'certificate': equilibrium_cert.name, 'certificate_sha256': sha(equilibrium_cert),
                'certificate_status': equilibrium_data['status'],
                'certificate_pins_checked': ['producer_sha256'], 'finite_check_count': 18,
                'certificate_scope': equilibrium_data['scope'],
                'new_this_round_first_execution_only': True})
paired_aux_script = local('cdt_odd_paired_head_free_auxiliary_prime_20261006_verify.py')
paired_aux_cert = local('cdt_odd_paired_head_free_auxiliary_prime_20261006_verify.json')
paired_aux_data = json.loads(paired_aux_cert.read_text(encoding='utf-8'))
assert paired_aux_data['status'] == 'finite-exact-probe-only'
assert paired_aux_data['new_own_execution_count'] == 1
assert paired_aux_data['old_or_peer_execution_import_rerun_count'] == 0
assert paired_aux_data['all_checked_local_identities_passed'] is True
assert len(paired_aux_data['cases']) == 10
paired_aux_report = local('cdt_odd_paired_head_free_auxiliary_prime_20261006.md')
reports.append({'report': paired_aux_report.name, 'report_sha256': sha(paired_aux_report),
                'script': paired_aux_script.name, 'script_sha256': sha(paired_aux_script),
                'certificate': paired_aux_cert.name, 'certificate_sha256': sha(paired_aux_cert),
                'certificate_status': paired_aux_data['status'],
                'certificate_pins_checked': [], 'finite_check_count': 10,
                'certificate_scope': paired_aux_data['scope'],
                'new_this_round_first_execution_only': True})
new_proof_files += [
    'cdt_odd_paired_primitive_gcd_rate_20261006.md',
    'cdt_odd_paired_plucker_energy_rate_20261006.md',
    'cdt_odd_paired_all_prime_budget_20261006.md',
    'cdt_odd_paired_auxiliary_units_structure_20261006.md',
    'cdt_odd_paired_primitive_gcd_rate_independent_review_20261006.md',
    'cdt_odd_paired_all_prime_budget_independent_review_20261006.md',
    'cdt_odd_paired_auxiliary_units_structure_independent_review_20261006.md',
    'cdt_odd_paired_rate_units_budget_root_review_20261006.md',
]
new_proof_files += ['cdt_odd_paired_dual_plucker_carry_rate_20261006.md', 'cdt_odd_paired_large_prime_jet_rank_20261006.md', 'cdt_odd_paired_mirror_choice_energy_20261006.md', 'cdt_odd_paired_auxiliary_pade_symplectic_defect_20261006.md', 'cdt_odd_paired_dual_jet_budget_independent_review_20261006.md', 'cdt_odd_paired_mirror_choice_energy_independent_review_20261006.md', 'cdt_odd_paired_auxiliary_pade_symplectic_defect_independent_review_20261006.md', 'cdt_odd_paired_dual_carry_jet_mirror_root_review_20261006.md']
# These checks read saved certificates only; no producer is imported or executed.
paired_round_reports = [
    ('cdt_odd_paired_primitive_gcd_rate_20261006.md',
     'cdt_odd_paired_primitive_gcd_rate_20261006_verify.py',
     'cdt_odd_paired_primitive_gcd_rate_20261006_verify.json',
     'exact_piecewise_integral_and_tail_checks_passed'),
    ('cdt_odd_paired_plucker_energy_rate_20261006.md',
     'cdt_odd_paired_plucker_energy_rate_20261006_verify_v2.py',
     'cdt_odd_paired_plucker_energy_rate_20261006_verify_v2.json', 'PASS'),
    ('cdt_odd_paired_all_prime_budget_20261006.md',
     'cdt_odd_paired_all_prime_budget_verify_20261006.py',
     'cdt_odd_paired_all_prime_budget_verify_20261006.json', 'PASS'),
    ('cdt_odd_paired_auxiliary_units_structure_20261006.md',
     'cdt_odd_paired_auxiliary_units_structure_20261006_verify.py',
     'cdt_odd_paired_auxiliary_units_structure_20261006_verify.json',
     'finite-exact-structure-probe-only'),
]
paired_round_reports += [('cdt_odd_paired_dual_plucker_carry_rate_20261006.md', 'cdt_odd_paired_dual_plucker_layers_20261006_probe.py', 'cdt_odd_paired_dual_plucker_layers_20261006_probe.json', 'finite-exact-dual-plucker-probe-only'), ('cdt_odd_paired_dual_plucker_carry_rate_20261006.md', 'cdt_odd_paired_dual_plucker_carry_rate_20261006_verify_v2.py', 'cdt_odd_paired_dual_plucker_carry_rate_20261006_verify_v2.json', 'exact-dual-carry-rate-certificate-pass'), ('cdt_odd_paired_large_prime_jet_rank_20261006.md', 'cdt_odd_paired_large_prime_jet_rank_20261006_verify.py', 'cdt_odd_paired_large_prime_jet_rank_20261006_verify.json', 'PASS'), ('cdt_odd_paired_mirror_choice_energy_20261006.md', 'cdt_odd_paired_mirror_choice_energy_20261006_verify.py', 'cdt_odd_paired_mirror_choice_energy_20261006_verify.json', 'PASS'), ('cdt_odd_paired_auxiliary_pade_symplectic_defect_20261006.md', 'cdt_odd_paired_auxiliary_pade_symplectic_defect_20261006_verify.py', 'cdt_odd_paired_auxiliary_pade_symplectic_defect_20261006_verify.json', 'PASS finite structural mechanism only')]
paired_round_reports += [('cdt_odd_paired_residue_crt_integral_model_20261006.md', 'cdt_odd_paired_residue_crt_integral_model_20261006_verify.py', 'cdt_odd_paired_residue_crt_integral_model_20261006_verify.json', 'finite-exact-residue-CRT-mechanism-pass'), ('cdt_odd_paired_second_smith_layer_20261006.md', 'cdt_odd_paired_second_smith_layer_20261006_verify.py', 'cdt_odd_paired_second_smith_layer_20261006_verify.json', 'PASS'), ('cdt_odd_paired_smith_credit_cap_transfer_20261006.md', 'cdt_odd_paired_smith_credit_cap_transfer_20261006_verify.py', 'cdt_odd_paired_smith_credit_cap_transfer_20261006_verify.json', 'PASS'), ('cdt_odd_paired_auxiliary_boundary_jacobi_krylov_20261006.md', 'cdt_odd_paired_auxiliary_boundary_jacobi_krylov_20261006_verify.py', 'cdt_odd_paired_auxiliary_boundary_jacobi_krylov_20261006_verify.json', 'PASS')]
for report_name, script_name, cert_name, expected_status in paired_round_reports:
    cert_data = json.loads(local(cert_name).read_text(encoding='utf-8'))
    assert cert_data['status'] == expected_status, cert_name
    pins_checked = []
    if 'producer_sha256' in cert_data:
        assert cert_data['producer_sha256'] == sha(local(script_name)), cert_name
        pins_checked.append('producer_sha256')
    reports.append({'report': report_name, 'report_sha256': sha(local(report_name)),
                    'script': script_name, 'script_sha256': sha(local(script_name)),
                    'certificate': cert_name, 'certificate_sha256': sha(local(cert_name)),
                    'certificate_status': cert_data['status'],
                    'certificate_pins_checked': pins_checked,
                    'certificate_scope': cert_data['scope'],
                    'new_this_round_first_execution_only': True})
# Saved NEW certificates only; no mathematical source is executed or imported.
new_support_round_stems = ['cdt_odd_paired_support_correlated_budget_20261006', 'cdt_odd_paired_actual_local_gram_layers_20261006', 'cdt_odd_paired_weighted_jet_support_budget_20261006', 'cdt_odd_paired_jacobi_modified_target_normality_20261006']
new_support_round_stems += [
    'cdt_odd_paired_actual_unit_sector_rank_20261006',
    'cdt_odd_paired_weighted_jet_global_optimization_20261006',
    'cdt_odd_paired_single_bordered_nonzero_gate_20261006',
    'cdt_odd_paired_fixed_middle_gosper_reduction_20261006',
]
new_support_round_stems += [
    'cdt_odd_paired_selected_jet_primitive_support_20261006',
    'cdt_odd_paired_supported_weighted_dual_transfer_20261006',
    'cdt_odd_paired_value_gram_depth4_nonzero_20261006',
    'cdt_odd_paired_fixed_middle_racah_border_20261006',
]
for stem in new_support_round_stems:
    report_name, script_name, cert_name = stem+'.md', stem+'_verify.py', stem+'_verify.json'
    cert_data = json.loads(local(cert_name).read_text(encoding='utf-8'))
    cert_status = cert_data.get('status', cert_data.get('state'))
    assert cert_status in {'PASS', 'PASS_FIRST1'}, cert_name
    certificate_scope = cert_data.get('scope', cert_data.get('finite_scope', cert_data.get('exact_domain')))
    if certificate_scope is None and stem == 'cdt_odd_paired_actual_unit_sector_rank_20261006':
        certificate_scope = 'Finite actual primitive Newton/paired value and scaled-derivative mechanism: n<=28, prime7<=p<=2n,p2>8n;143cases,91exactQ>=a+1 and52cap-only. Written all-scale proof separate; no infinite target normality.'
    if certificate_scope is None and stem == 'cdt_odd_paired_value_gram_depth4_nonzero_20261006':
        certificate_scope = 'Actual original-S normalized value-Gram at old r1,2,4 and general symmetric depth4/depth5 toys;66037checks. Actual anchor higher Smith not computed; no infinite nonzero assertion.'
    certificate_pins = []
    if 'source_sha256' in cert_data:
        assert cert_data['source_sha256'] == sha(local(script_name)), cert_name
        certificate_pins.append('source_sha256')
    reports.append({'report': report_name, 'report_sha256': sha(local(report_name)),
                    'script': script_name, 'script_sha256': sha(local(script_name)),
                    'certificate': cert_name, 'certificate_sha256': sha(local(cert_name)),
                    'certificate_status': cert_status, 'certificate_pins_checked': certificate_pins,
                    'certificate_scope': certificate_scope,
                    'new_this_round_first_execution_only': True})
assert not (RESEARCH / 'cdt_odd_paired_plucker_energy_rate_20261006_verify.json').exists()
assert not (RESEARCH / 'cdt_odd_paired_dual_plucker_carry_rate_20261006_verify.json').exists()
new_proof_files += ['cdt_odd_paired_residue_crt_integral_model_20261006.md', 'cdt_odd_paired_residue_crt_integral_model_independent_review_20261006.md', 'cdt_odd_paired_second_smith_layer_20261006.md', 'cdt_odd_paired_smith_credit_cap_transfer_20261006.md', 'cdt_odd_paired_auxiliary_boundary_jacobi_krylov_20261006.md', 'cdt_odd_paired_auxiliary_boundary_jacobi_krylov_independent_review_20261006.md', 'cdt_odd_paired_crt_smith_jacobi_root_review_20261006.md', 'cdt_odd_paired_smith_credit_cap_transfer_independent_review_20261006.md']
new_proof_files += ['cdt_odd_paired_support_correlated_budget_20261006.md', 'cdt_odd_paired_actual_local_gram_layers_20261006.md', 'cdt_odd_paired_weighted_jet_support_budget_20261006.md', 'cdt_odd_paired_jacobi_modified_target_normality_20261006.md', 'cdt_odd_paired_support_gram_modified_target_root_review_20261006.md', 'cdt_odd_paired_weighted_jet_support_budget_independent_review_20261006.md', 'cdt_odd_paired_direct_gram_support_independent_review_20261006.md', 'cdt_odd_paired_jacobi_modified_target_normality_independent_review_20261006.md']
new_proof_files += [
    'cdt_odd_paired_actual_unit_sector_rank_20261006.md',
    'cdt_odd_paired_weighted_jet_global_optimization_20261006.md',
    'cdt_odd_paired_single_bordered_nonzero_gate_20261006.md',
    'cdt_odd_paired_fixed_middle_gosper_reduction_20261006.md',
    'cdt_odd_paired_single_bordered_nonzero_gate_independent_review_20261006.md',
    'cdt_odd_paired_unit_sector_flow_independent_review_20261006.md',
    'cdt_odd_paired_fixed_middle_gosper_reduction_independent_review_20261006.md',
    'cdt_odd_paired_rank_flow_gosper_root_review_20261006.md',
]
new_proof_files += [
    'cdt_odd_paired_selected_jet_primitive_support_20261006.md',
    'cdt_odd_paired_supported_weighted_dual_transfer_20261006.md',
    'cdt_odd_paired_value_gram_depth4_nonzero_20261006.md',
    'cdt_odd_paired_fixed_middle_racah_border_20261006.md',
    'cdt_odd_paired_value_gram_depth4_nonzero_independent_review_20261006.md',
    'cdt_odd_paired_supported_jet_transfer_independent_review_20261006.md',
    'cdt_odd_paired_fixed_middle_racah_border_independent_review_20261006.md',
    'cdt_odd_paired_supported_racah_depth4_root_review_20261006.md',
]
assert len(new_proof_files) == 183
assert len(reports) == 108
assert len(current_frozen) == 424  # 16 math records plus 1 immutable FIRST1 guard
proofs = [{'file': name, 'sha256': sha(local(name))} for name in new_proof_files]

manifest_names = [
    'manifest_cdt_odd_20261005.json',
    'manifest_cdt_odd_background_20261005.json',
    'manifest_cdt_odd_level20_leaf_20261006.json',
    'manifest_cdt_odd_hasse_20261006.json',
    'manifest_cdt_odd_hasse_review_20261006.json',
    'manifest_cdt_odd_cartier_primary_20261006.json',
    'manifest_cdt_odd_external_draft_20261006.json',
    'manifest_cdt_candidates_5_8_12_20261006.json',
    'manifest_cdt_odd_uniformization_20261006.json',
    'manifest_cdt_odd_affine_galois_20261006.json',
    'manifest_cdt_odd_stabilizer_boundary_20261006.json',
    'manifest_cdt_odd_dedekind_stabilizer_20261006.json',
    'manifest_cdt_odd_hodge_bundle_20261006.json',
    'manifest_cdt_odd_classical_projection_20261006.json',
    'manifest_cdt_odd_eisenstein_extension_20261006.json',
    'manifest_cdt_odd_spin_geometry_20261006.json',
    'manifest_cdt_odd_connection_primary_20261006.json',
    'manifest_cdt_odd_classical_lambda_leaf_20261006.json',
    'cdt_odd_level12_cusp_space_primary_20261006.json',
]
manifest_names += ['manifest_cdt_odd_bailey_confluence_20261006.json', 'manifest_cdt_odd_classical_conifold_calibration_20261006.json', 'manifest_cdt_odd_classical_frobenius_smith_20261006.json', 'cdt_odd_level12_manin_period_primary_20261006.json', 'manifest_cdt_odd_classical_hypertrigonometry_20261006.json']
manifest_names += [
    'manifest_cdt_odd_R0_normal_function_20261006.json',
    'cdt_odd_level12_trivial_period_primary_20261006.json',
    'manifest_cdt_odd_ehmm_special_fiber_20261006.json',
]
manifest_names += [
    'manifest_cdt_odd_ehmm_2026_projection_20261006.json',
    'manifest_cdt_odd_R0_relative_cycle_20261006.json',
]
manifest_names += [
    'manifest_cdt_odd_conifold_arithmetic_20261006.json',
    'manifest_cdt_odd_quarter_actual_rank19_20261006.json',
    'manifest_cdt_odd_R0_toric_completion_20261006.json',
    'manifest_cdt_odd_weight_one_higher_chow_20261006.json',
]
manifest_names += [
    'manifest_cdt_odd_R0_klm_current_interface_20261006.json',
    'manifest_cdt_odd_R0_regulator_derivative_20261006.json',
    'manifest_cdt_odd_R0_Yukawa_scalar_interface_20261006.json',
]
manifest_names += ['manifest_cdt_odd_R0_compact_positive_cut_class_20261006.json']
manifest_names += [
    'manifest_cdt_odd_R0_noncompact_Tate_boundary_period_20261006.json',
    'manifest_cdt_odd_R0_positive_cut_boundary_flux_20261006.json',
]
manifest_names += [
    'manifest_cdt_odd_R0_conifold_effective_denominator_20261006.json',
    'manifest_cdt_odd_R0_regulator_Betti_extension_flag_20261006.json',
    'manifest_cdt_odd_R0_endpoint_flag_holonomy_interface_20261006.json',
    'manifest_cdt_odd_R0_toric_odd_prime_smooth_model_20261006.json',
    'manifest_cdt_odd_R0_all_odd_generic_radius_arithmetic_interface_20261006.json',
]
manifest_names += [
    'manifest_cdt_odd_2026_polylog_primary_sources_20261006.json',
    'manifest_cdt_odd_lai2026_mixed_zeta_20261006.json',
    'manifest_cdt_odd_R0_logarithmic_flag_slopes_reduction_20261006.json',
    'manifest_cdt_odd_R0_nonlinear_projective_invariant_field_20261006.json',
]
manifest_pins = {
    'manifest_cdt_odd_R0_all_odd_generic_radius_arithmetic_interface_20261006.json': '775149ca7c34a3f80fedf8a0a59e65bfa08edf76273ce0562b0f42486aeccb88',
    'manifest_cdt_odd_R0_conifold_effective_denominator_20261006.json': 'b3c7ff3c54c030e806750395ae115d43f997576c7aa457d3bcad3c3e3c11569c',
    'manifest_cdt_odd_R0_regulator_Betti_extension_flag_20261006.json': '8cc416a01de0f5e75724205f33dfd25930d6d449109070e2bdbd097127f3d208',
    'manifest_cdt_odd_R0_endpoint_flag_holonomy_interface_20261006.json': '2d53adc254d713b1343cc6519306e724e23ceacfae68b8344ecb1141c46bed82',
    'manifest_cdt_odd_R0_toric_odd_prime_smooth_model_20261006.json': 'bcf77395a646e8d120e6322c622d7c56bdbe1e16c0bbd13a8ed5cae22f1ca737',
    'manifest_cdt_odd_R0_noncompact_Tate_boundary_period_20261006.json': '8fe7613aa93e9809da5f22006401320efe4db8ed733a6e2db67efc3dd1791e8e',
    'manifest_cdt_odd_R0_positive_cut_boundary_flux_20261006.json': 'ca236fccf8c352218e0b572110a243e3d4789f5477d155d700845a745ba522c2',
    'manifest_cdt_odd_R0_compact_positive_cut_class_20261006.json': '7c8f068d19d6ed73843b7a4b09413d64ece616ada448b35ce019f369fa6068a2',
    'manifest_cdt_odd_R0_klm_current_interface_20261006.json': '1b5e83273c5ac85cce91e79dcfb671eed1ddf733340c15fac0ca0add2ac1ca61',
    'manifest_cdt_odd_R0_regulator_derivative_20261006.json': 'db7eb01a5469fd58c7e16454604f88fd87f26b5353922c7546b37e6949773f95',
    'manifest_cdt_odd_R0_Yukawa_scalar_interface_20261006.json': 'ae690668ee491d2f3b34f07245d3ec5647a4bd8881aa1f5a3109e83b5d08e121',
    'manifest_cdt_odd_conifold_arithmetic_20261006.json': 'eba2c4f8ea07f150c673a6190afe6c3a86c8815e858e8174981c5ca999f47b84',
    'manifest_cdt_odd_quarter_actual_rank19_20261006.json': '49936b70d2f17daafb7e9b871e2ec2559d1eaf40262c44b4416b3a2e4738c1f4',
    'manifest_cdt_odd_R0_toric_completion_20261006.json': '509b0b5205e21b38dd8383f14a95a3fcae173e24aad1a6addbcb21f2f9e298b6',
    'manifest_cdt_odd_weight_one_higher_chow_20261006.json': 'a82c6465281cfe036854180709cfa73bd13113005c055dbdea7609f8608f7500',
    'manifest_cdt_odd_ehmm_2026_projection_20261006.json': '57a4b45c476e75312983b2abf6733a48e567dc5353ef98342a6b2fe6fbea9108',
    'manifest_cdt_odd_R0_relative_cycle_20261006.json': 'd1a9d025241b1b59ab9b3c90ce0453b623d48a96b394bd77b1a7905bd8f1b19c',
    'manifest_cdt_odd_R0_normal_function_20261006.json': '6ef75e211bc4a9d5ddbb479516eca54e9bbaa2653d3a00f6bab76075ed8ad0d4',
    'cdt_odd_level12_trivial_period_primary_20261006.json': 'ab59a2bf279994125a25b7ed4195d8ca204cd32005501777fa17052630b04888',
    'manifest_cdt_odd_ehmm_special_fiber_20261006.json': '8719e5d2bd5c2264b032ac1dbf415f00f5a64ad0e1acfa9d375f35e741ca898e',
    'manifest_cdt_odd_bailey_confluence_20261006.json': '14ccd025dda885182e4c34bab081069ceda1ab476ec480f4c871ac2b7ea4daef',
    'manifest_cdt_odd_classical_conifold_calibration_20261006.json': '418e2a4181bb6a94419265a582f5b809af50cf2cbe5f13bf6300f8aca95b567f',
    'manifest_cdt_odd_classical_frobenius_smith_20261006.json': '124d7da44f73ae6930bf3554ed0e93fda7c51d89d7a308b7ef8da4a6bf2a668b',
    'cdt_odd_level12_manin_period_primary_20261006.json': '71c145aaf6d405a2ed5a919424bc498028b4aca72059139d131672153ba3e5ca',
    'manifest_cdt_odd_classical_hypertrigonometry_20261006.json': '34d6c0539e32b504e621a0a4f323a39c3074ae416aa698b135a3467bae95d32e',

    'manifest_cdt_odd_connection_primary_20261006.json':
        '79d144854c2153748aba23de764d95abfe6ec3442a85fa493d275872aa75fca8',
    'manifest_cdt_odd_classical_lambda_leaf_20261006.json':
        '70ee1c55d38f53504c65adece80186453814f52c5af118b2958abc4ab5d17589',
    'cdt_odd_level12_cusp_space_primary_20261006.json':
        '454fec33d60db3d49a8b47f4b39779387872f3b27f88a4a78c6d59e6489349a0',
    'manifest_cdt_odd_spin_geometry_20261006.json':
        '54c69a986dc5fedb3b1f773f59a2a6d16c56cdc95594902fcc2e58fc8eacd745',
    'manifest_cdt_odd_cartier_primary_20261006.json':
        'ed5f5c302ce9dae1ac9b13da280df61dba08a9f132a766747e7a158a38743969',
    'manifest_cdt_odd_external_draft_20261006.json':
        '270bff28a4887e300d1f914578f7617870948216f000b7eb6afc10b8214dacd0',
    'manifest_cdt_candidates_5_8_12_20261006.json':
        'f6302e54ca2fe93ebe11b8d2ad0502ac0c60d30eebb75acd393ef34184adb92c',
    'manifest_cdt_odd_uniformization_20261006.json':
        'b2384cefdad9f2de4a2f012ea934346324a90364624c30616d3d3c520c263d89',
    'manifest_cdt_odd_affine_galois_20261006.json':
        '8f00d2aec859e73c9a9968868a30b1d51bea5a0c787af628abf8a8e24fcb2775',
    'manifest_cdt_odd_stabilizer_boundary_20261006.json':
        '0290de83a7b31deac1cde91f68c749a8c26073ac865756f3040368f2b7b39b62',
    'manifest_cdt_odd_dedekind_stabilizer_20261006.json':
        '329c898b30f0e339bc7859244fccaf0c2ee69129d42b3ad714e35001ce5cb867',
    'manifest_cdt_odd_hodge_bundle_20261006.json':
        '3cc01008db8b38df7559d0bdc99d507620541fd0427d2b34d7bf513a4be208f2',
    'manifest_cdt_odd_classical_projection_20261006.json':
        '79480aa2ec383e72f3d4f2655fdd21868751f5c39fc2b360c28bc7e2163f4506',
    'manifest_cdt_odd_eisenstein_extension_20261006.json':
        '345e4de363594c73a2b08c4cae8644ffa0ac1a8bc6e53fbba10f3d2ea1e2bf9b',
}
manifest_pins.update({
    'manifest_cdt_odd_2026_polylog_primary_sources_20261006.json': '8c82166ffd46ada438f5726bf34cb575a3edef49e5da3c7165f54cc7fced4c86',
    'manifest_cdt_odd_lai2026_mixed_zeta_20261006.json': '9763dff18ed5b23001220a6081e158570aeff766075177082acd35f2f7a50609',
    'manifest_cdt_odd_R0_logarithmic_flag_slopes_reduction_20261006.json': 'f55d8f15ce967f864cf85b5b6fa1971dc98369aada6829cbf7f9e4ceb8e060ac',
    'manifest_cdt_odd_R0_nonlinear_projective_invariant_field_20261006.json': 'b76e6d36b85f3e93c12c92cf0856a46b49a89270e304803f1d3561b5de47d17d',
})
manifest_names += [
    'manifest_cdt_odd_mixed_double_pole_arithmetic_cost_20261006.json',
    'manifest_cdt_odd_mixed_double_pole_analytic_decay_20261006.json',
    'manifest_cdt_odd_mixed_double_pole_primitive_lattice_20261006.json',
    'manifest_cdt_odd_double_pole_layout_budget_root_20261006.json',
]
manifest_pins.update({
    'manifest_cdt_odd_mixed_double_pole_arithmetic_cost_20261006.json': '6a78cda6cf7517cdf47a83548a7974a305dc561b46b99176d0cf8a325dfaaa88',
    'manifest_cdt_odd_mixed_double_pole_analytic_decay_20261006.json': '3fa8dfa9dfdb0fd1cbcabc3ecd29def1a3f8b9402b127079fedfa8ca6eca0b25',
    'manifest_cdt_odd_mixed_double_pole_primitive_lattice_20261006.json': '1cd31148e2b10f5f0878e697681b202f5d33e7ca77b6bb272c4059e5dff8b0e3',
    'manifest_cdt_odd_double_pole_layout_budget_root_20261006.json': 'e7ed6ffab26fc7e75f16677f9f31ea295739df2e7d589fdef8e68ef77a13cda8',
})
manifest_names += [
    'manifest_cdt_odd_paired_head_free_integral_lattice_20261006.json',
    'manifest_cdt_odd_paired_head_free_auxiliary_prime_20261006.json',
    'manifest_cdt_odd_paired_analytic_equilibrium_root_20261006.json',
    'manifest_cdt_odd_restored_zero_equilibrium_energy_20261006.json',
]
manifest_pins.update({
    'manifest_cdt_odd_paired_head_free_integral_lattice_20261006.json': '6d2d7deddd4837840d5b33c535659523196cbe3e59ec021fb4189bcc6878bb84',
    'manifest_cdt_odd_paired_head_free_auxiliary_prime_20261006.json': '1c35ae09a7260786373840ff288f7dec09f210994aa1ca3908edfd5ed048c419',
    'manifest_cdt_odd_paired_analytic_equilibrium_root_20261006.json': 'b92ef465617f7f48bac0101bdf06b2f0d83538ed64eebce568364896e00be256',
    'manifest_cdt_odd_restored_zero_equilibrium_energy_20261006.json': '190642d5d8a5c0fc02c60942fb4937da2dc564956819588db19a8980961cdf98',
})
manifest_names += [
    'manifest_cdt_odd_paired_rate_units_budget_root_20261006.json',
    'manifest_cdt_odd_paired_plucker_energy_rate_20261006.json',
    'manifest_cdt_odd_paired_all_prime_budget_20261006.json',
    'manifest_cdt_odd_paired_auxiliary_units_structure_20261006.json',
]
manifest_pins.update({
    'manifest_cdt_odd_paired_rate_units_budget_root_20261006.json': '490d6304e165d98fecae2fc84f7e30a4de90e92bb348ab46312fd85ca2cf4eef',
    'manifest_cdt_odd_paired_plucker_energy_rate_20261006.json': 'f7750d5b85719565ef7e9a4cc4d246f1f8a3806cb07a05c4f59221596e0d8efa',
    'manifest_cdt_odd_paired_all_prime_budget_20261006.json': 'e8da21a80cd7a67e6ea9dfdfa95a054b49a8508ada547e46082c5bd5d9c296a5',
    'manifest_cdt_odd_paired_auxiliary_units_structure_20261006.json': '244b2c872e16a01a1822a095b87636e32475238a2e657683c1d12371aa701a4f',
})
# Final dual-carry/jet/mirror/symplectic source receipts
manifest_names += ['manifest_cdt_odd_paired_dual_carry_jet_mirror_root_20261006.json', 'manifest_cdt_odd_paired_mirror_choice_energy_20261006.json', 'manifest_cdt_odd_paired_large_prime_jet_rank_20261006.json', 'manifest_cdt_odd_paired_auxiliary_pade_symplectic_defect_20261006.json']
manifest_pins.update({'manifest_cdt_odd_paired_dual_carry_jet_mirror_root_20261006.json': '148d09dce421ceb560bfd0080916826954980586f647f764af35b943a29c6e17', 'manifest_cdt_odd_paired_mirror_choice_energy_20261006.json': '8fd3078e221220d293191e716673e45c582b7592ae9f76a4bfcd100263b796fc', 'manifest_cdt_odd_paired_large_prime_jet_rank_20261006.json': '9683b3c80fcc2cc512d31d7ba144b27936d8fcf4885ff4222f38369393fec746', 'manifest_cdt_odd_paired_auxiliary_pade_symplectic_defect_20261006.json': 'f0502fc3539c08c95aa979c502eb5bda26d8c467734eb406e58ac68304d417da'})
# NEW final CRT/Smith/Jacobi source receipts actually read and frozen.
manifest_names += ['manifest_cdt_odd_paired_residue_crt_layers_root_20261006.json', 'manifest_cdt_odd_paired_second_smith_layer_20261006.json', 'manifest_cdt_odd_paired_smith_credit_cap_transfer_20261006.json', 'manifest_cdt_odd_paired_auxiliary_boundary_jacobi_krylov_20261006.json']
manifest_pins.update({'manifest_cdt_odd_paired_residue_crt_layers_root_20261006.json': 'd315edb66f9c7b3eb7423563a0010772c772a2b5519afc6ebfce6c609f158427', 'manifest_cdt_odd_paired_second_smith_layer_20261006.json': '556c65c263154a25e24d93c859a2750460a01eef6d65f8ab1e9e0a94d2678f3e', 'manifest_cdt_odd_paired_smith_credit_cap_transfer_20261006.json': 'f8c73f780da60d04a30f484189b9d4004b3ddf5f543b988857d8cffd1d5b3542', 'manifest_cdt_odd_paired_auxiliary_boundary_jacobi_krylov_20261006.json': '129070562e4df36e5e0fcfb2b93202bf9d4b015d287fb04ced89bac556a2e1b3'})
# NEW final source receipts actually fully read by root, one-way pins.
manifest_names += ['manifest_cdt_odd_paired_weighted_support_modified_target_root_20261006.json', 'manifest_cdt_odd_paired_support_correlated_budget_20261006.json', 'manifest_cdt_odd_paired_actual_local_gram_layers_20261006.json', 'manifest_cdt_odd_paired_jacobi_modified_target_normality_20261006.json']
manifest_pins.update({'manifest_cdt_odd_paired_weighted_support_modified_target_root_20261006.json': '3a29ea816741a59bc70a45878c3edb7cde889e9551eb530cea2caefd5ce2e364', 'manifest_cdt_odd_paired_support_correlated_budget_20261006.json': '09d18115750b9488813a6c328c08373d8d939eefb92c199aa458727a0a4d54b9', 'manifest_cdt_odd_paired_actual_local_gram_layers_20261006.json': '4086d265702b4a4798eef796579758aeb3c62e997d0b4c51bc934cbd0235f5ce', 'manifest_cdt_odd_paired_jacobi_modified_target_normality_20261006.json': 'fa77214875c2beb909739791013054c8dbff87cbf9c587768e1ad2be8295fd4d'})
latest_rank_flow_gate_gosper_manifest_pins = {
    'manifest_cdt_odd_paired_rank_flow_single_gate_gosper_root_20261006.json': 'd5de8fd0238d7ea6319af7d477cfa7ba377b22b11f44392fcc180d2ad966982f',
    'manifest_cdt_odd_paired_actual_unit_sector_rank_20261006.json': '46cd08a4bb3bc229ffd58c19e444d281d20565af5884b70e8619d047c1a59852',
    'manifest_cdt_odd_paired_weighted_jet_global_optimization_20261006.json': '90b3df0100c798c909866d4aba694b31c67dac024e22d0ef1a061acad41ab552',
    'manifest_cdt_odd_paired_fixed_middle_gosper_reduction_20261006.json': 'fc826fd1f7b5ae84afaf21e416c723de4de311d75ebf2c0addcd7aa7f8d20f9b',
    'manifest_cdt_odd_paired_fixed_middle_gosper_final_review_pins_20261006.json': '5f1ea44de2c8da159c5d28c05f9a8360a0d1c0dc7eac972519033e3e05a6690e',
}
manifest_names += list(latest_rank_flow_gate_gosper_manifest_pins)
manifest_pins.update(latest_rank_flow_gate_gosper_manifest_pins)
# Final supported/Racah/depth4 source receipts, after actual full final reads.
latest_supported_racah_depth4_manifest_pins = {'manifest_cdt_odd_paired_selected_jet_primitive_support_20261006.json': '893e384530589795701cf8506650547a118042c5632d18486e910b6d7113eedc', 'manifest_cdt_odd_paired_supported_weighted_dual_transfer_20261006.json': 'a286feded461742efb471990c277f22a3c111401d6f321b31c6399e4a0f2f25c', 'manifest_cdt_odd_paired_fixed_middle_racah_border_20261006.json': 'a5ac5eb90cfbc43057f69a5f0d21b000af1dd672d0a7299015c085e89a62f1fa', 'manifest_cdt_odd_paired_supported_racah_depth4_root_20261006.json': '646c34c4c34fb45092b2c9b4d4f173f7dc225ba063ec02e541638cc9e3853663'}
manifest_names += list(latest_supported_racah_depth4_manifest_pins)
manifest_pins.update(latest_supported_racah_depth4_manifest_pins)
for name, expected in manifest_pins.items():
    assert sha(local(name, ROOT / 'literature')) == expected, name
external_snapshot_pins = {
    'long2026_hybrid_arithmetic_holonomy_draft_20261006.tex':
        'f4d8e0582d3ce3ca88d0553b9ae5a212007fc01da169188d22ed3e0311974fd3',
    'long2026_hybrid_issue1_20261006.json':
        'd5df7f8e04809a908cc599d329207cdd7f61c291041a406dfb34b8eede98286c',
}
external_snapshots = []
for name, expected in external_snapshot_pins.items():
    assert sha(local(name, ROOT / 'literature')) == expected, name
    external_snapshots.append({'file': name, 'sha256': expected,
                               'status': 'unverified_research_draft_or_public_issue_snapshot'})
pdfs = {}
non_pdf_primary = {}
source_code_primary = {}


def collect(value):
    if isinstance(value, list):
        for child in value:
            collect(child)
    elif isinstance(value, dict):
        name = value.get('file') or value.get('path') or value.get('filename') or value.get('local_path') or value.get('local_file')
        expected = value.get('sha256')
        if isinstance(name, str) and name.lower().endswith('.pdf') and expected:
            path = (ROOT / name).resolve()
            if not path.is_file():
                path = local(Path(name).name, ROOT / 'literature')
            assert path.is_relative_to(ROOT), str(path)
            actual = sha(path)
            assert actual == expected, name
            earlier = pdfs.get(path.name, {})
            pages = value.get('pages', value.get('pdf_pages'))
            version = value.get('version', value.get('arxiv_version', value.get('version_scope', value.get('fixed_version', value.get('version_observed')))))
            pdfs[path.name] = {'file': str(path.relative_to(ROOT)).replace('\\', '/'),
                               'sha256': actual,
                               'pages': pages if pages is not None else earlier.get('pages'),
                               'version': version if version is not None else earlier.get('version')}
        elif (isinstance(name, str) and expected
              and name.replace('\\', '/').startswith('literature/')
              and Path(name).suffix.lower() in {'.lean', '.md'}):
            path = (ROOT / name).resolve()
            assert path.is_relative_to(ROOT) and path.is_file(), name
            assert sha(path) == expected, name
            source_code_primary[name] = {
                'file': name, 'sha256': expected,
                'commit': value.get('commit'),
                'actual_reading_scope': value.get('actual_reading_scope'),
                'execution_count': value.get('execution_count'),
            }
        elif isinstance(name, str) and name.lower().endswith('.html') and expected:
            path = (ROOT / name).resolve()
            if not path.is_file():
                path = local(Path(name).name, ROOT / 'literature')
            assert path.is_relative_to(ROOT), str(path)
            actual = sha(path)
            assert actual == expected, name
            non_pdf_primary[path.name] = {
                'file': str(path.relative_to(ROOT)).replace('\\', '/'),
                'sha256': actual, 'version': value.get('version'),
                'actual_read': value.get('actual_read'),
            }
        for child in value.values():
            if isinstance(child, (dict, list)):
                collect(child)


for name in manifest_names:
    collect(json.loads(local(name, ROOT / 'literature').read_text(encoding='utf-8')))

links = 0
for path in [local('cdt_odd_background_progress_20261006.md')] + [local(n) for n in new_proof_files] + [local(r['report']) for r in reports]:
    for target in re.findall(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)', path.read_text(encoding='utf-8')):
        if ':' in target or target.startswith('#'):
            continue
        target = target.split('#', 1)[0]
        if not target:
            continue
        # Markdown-like substrings also occur in LaTeX products such as
        # [Af](Af). Check file references, not mathematical parentheses.
        if Path(target).suffix.lower() not in {'.md', '.pdf', '.py', '.json', '.tex', '.png', '.html'}:
            continue
        assert (path.parent / target).resolve().is_file(), (path.name, target)
        links += 1

out = {
    'status': 'file_provenance_checks_passed',
    'as_of': '2026-10-06',
    'checked_at_utc': datetime.now(timezone.utc).isoformat(),
    'main_report': 'cdt_odd_background_progress_20261006.md',
    'main_report_sha256': sha(local('cdt_odd_background_progress_20261006.md')),
    'reports': reports,
    'large_prime_square_probe': square_probe,
    'new_proof_and_review_files': proofs,
    'earlier_frozen_files_checked': frozen,
    'current_frozen_inputs_checked': current_frozen,
    'original_source_pdfs': list(pdfs.values()),
    'original_source_html_snapshots': list(non_pdf_primary.values()),
    'original_source_code_snapshots': list(source_code_primary.values()),
    'original_pdf_pages': sum(p['pages'] for p in pdfs.values() if isinstance(p['pages'], int)),
    'original_unique_pdf_content_count': len({p['sha256'] for p in pdfs.values()}),
    'original_unique_pdf_content_pages': sum({p['sha256']:p['pages'] for p in pdfs.values() if isinstance(p['pages'],int)}.values()),
    'original_pdf_count_scope': 'Archive filenames count separately; identical-content BK author/alternate archives already existed in prior74. Unique-content counters deduplicate by SHA256. Newly registered existing20-page CDT primary is not a new download.',
    'unverified_external_draft_snapshots': external_snapshots,
    'local_links_checked': links,
    'scope': 'Previous Level20 Hasse/Frobenius, actual rank19 closure, scoped native S2, Cartier primitives and mixed Bockstein results are preserved; no successful Level20 mixed S2 is claimed. Level8 specified conjugate Tate obstruction is preserved. Level12 now has full finite Gamma-cusp regularization and rational Tate cocycles for both actual targets, a complete rank9 free Gamma presentation and Gamma semidirect C2 extension, all nine actual period vectors, and integral GL4 right affine holonomy whose origin stabilizer is exactly the same scalar target stabilizer. The full stabilizer is not classified. Every fixed nontrivial rational relation between 1,zeta3,L3(chi12) has paired integral coordinates, actual rank4 closure, full prefix denominator rate3 and the stated componentwise Euler-array lower bound; no arbitrary mixed-lattice lower bound or joint Up identity is claimed. Real T/W and T/M/Mprime leaves, fixed derivative gauges, three cusp logs and actual ranks13/23 persist throughout that relation family. Exact original costs366/169 and1146/529 and Green mean bounds6/5 and5/4 exclude the two fixed plain-CDT arrays on the proved leaves. Pure-L fixed-original-lattice S1 credit gamma1=1/2 is proved in its matching window. Characteristic-p log zero estimates decouple S1/S2 in the stated windows; fixed target S2 lifts have an explicit S3 background obstruction, not a successful S2/S3 construction. Even cap3 credit given fully in the same p<=D matching window fails ordinary Jensen for the fixed rank7/13/23 arrays; this does not cover outside-window credit, exponents>3, new models, or a separately proved refined numerator floor. Certificates only check declared finite identities and file provenance; written global proofs remain essential. No new numerical odd-zeta/L theorem or Lean formalization. The external p-adic draft remains unverified and no external manuscript source was executed.',
    'new_numerical_irrationality_theorem': False,
    'new_lean_formalization': False,
    'balanced_tensor_smith_bridge_proved': True,
    'balanced_tensor_scope': 'CDT Section 8 near-balanced source; specified arrays, theta-matching windows, and fixed integral cutoff before optimization.',
    'integrated_tensor_fixed_cutoff_bridge_proved': True,
    'real_target_integral_rank5_and_combined_rank14_proved': True,
    'six_kernel_actual_rank10_and_combined_rank19_proved': True,
    'all_good_prime_cartier_kernel_degree5_proved': True,
    'all_good_prime_hecke_kernel_dimension3_proved': True,
    'six_integral_full_depth1_hecke_matrix_proved': True,
    'native_integral_prefix_rank_exact_in_stated_windows': True,
    'pure_native_constant_s2_classification_proved': True,
    'pure_native_smith_exponents_zero_or_one_for_N_gt_p_plus_5': True,
    'raw_first_threshold_baseline_proved_in_stated_fixed_model': True,
    'same_nine_species_cap4_matching_window_optimistic_budget_fails': True,
    'bounded_rational_cartier_primitive_proved': True,
    'old_three_derivative_polynomial_primitive_representation_proved': True,
    'q_coordinate_mixed_bockstein_remainder_explicit': True,
    'safe_mixed_multiplier_second_layer_budget_upper_bound_proved': True,
    'five_existing_background_full_slow_packets_proved': True,
    'five_background_own_rank5_unit_minor_proved': True,
    'five_background_disjoint_from_hecke_image_proved': True,
    'five_background_disjointness_scope': 'Eleven actual slow columns; specified good-prime native and polynomial prefix windows. Not all degrees, primes, or prefixes.',
    'D5_D8_D12_candidate_period_sources_proved': True,
    'level32_fricke_eta_hauptmodul_proved': True,
    'low_level_mixed_candidates_common_leaf_proved': False,
    'level8_specified_three_source_pure_projection_obstructed': True,
    'level12_real_pure_L3_and_zeta3_period_sources_proved': True,
    'level12_all_integer_relation_period_trigger_proved': True,
    'level12_paired_all_order_integral_coordinates_proved': True,
    'level12_target_actual_rank4_proved': True,
    'level12_componentwise_pure_L_denominator_rate3_proved': True,
    'level12_all_relation_full_prefix_denominator_rate3_proved': True,
    'level12_all_relation_componentwise_Euler_array_lower_bound_proved': True,
    'level12_all_relation_full_joint_model_proved': True,
    'level12_joint_source_full_Up_identity_proved': False,
    'level12_joint_mixed_nonzero_B_C_kernel_is_two_actual_kernels_intersection': True,
    'level12_full_real_hecke_leaves_and_derivative_gauges_proved': True,
    'level12_three_cusp_logs_algebraically_independent_proved': True,
    'level12_cheap_log_combined_actual_ranks': [13, 23],
    'level12_exact_original_CDT_transport_costs': ['366/169', '1146/529'],
    'level12_base_green_mean_log_radius_lt_6_over_5_proved': True,
    'level12_augmented_green_mean_log_radius_lt_5_over_4_proved': True,
    'level12_two_fixed_plain_CDT_arrays_fail_on_proved_leaves': True,
    'level12_signed_cocycle_entire_eta_reflection_family_nonzero_for_n_ne_0_proved': True,
    'level12_signed_cocycle_scope': 'Exact eta powers and J_n=eta^n M eta^(-n); nonzero for integer n!=0. n=0 has zero defect. No full stabilizer classification or general-word nonvanishing.',
    'level12_full_real_stabilizer_classified': False,
    'level12_character_tensor_fixed_packet_Taylor_and_period_obstructions_proved': True,
    'level12_character_tensor_new_algebraic_scalar_constructed': False,
    'level12_all_cusp_regularized_cocycle_formula_proved': True,
    'level12_all_Gamma_two_actual_rational_Tate_cocycles_proved': True,
    'level12_complete_Gamma_rank9_free_presentation_proved': True,
    'level12_complete_Gamma_semidirect_C2_presentation_proved': True,
    'level12_complete_nine_generator_two_actual_period_tables_proved': True,
    'level12_full_integer_period_lattice_Z_plus_Ztau_plus_12Ztau2_proved': True,
    'level12_actual_GL4Z_right_affine_holonomy_proved': True,
    'level12_affine_origin_stabilizer_equals_actual_scalar_stabilizer_proved': True,
    'level12_known_zero_group_is_complete_group_free_factor_proved': True,
    'level12_complete_free_product_structure': 'Gstar = H0 * F(x4,x5,x9), H0 = Z * C2 * C2',
    'level12_same_prefix_sign_infinite_word_strict_cone_exclusion_proved': True,
    'level12_strict_definite_translation_excludes_all_nonidentity_known_factor_conjugates_proved': True,
    'level12_cone_exclusion_scope': 'Actual pure-L signed affine translations; same epsilon(prefix)*sign(exponent) condition for every extra syllable. Strict definite b_g gives K_L intersect g H0 g^-1 = {1}. Indefinite, null, zero translations and mixed-sign cancellations are not classified.',
    'level12_eight_actual_Gamma_cusp_classes_all_conjugates_and_nonzero_powers_excluded': True,
    'level12_cusp_exclusion_scope': 'No-affine-fixed-point obstruction from nonzero actual source constant. Remaining two Gamma classes form one Gstar class with an affine-orbit/fixed-line condition; this does not count full K cusps.',
    'level12_full_cohomology_and_boundary_dimensions': [24, 10, 14],
    'level12_cohomology_class_does_not_determine_actual_origin_stabilizer_proved': True,
    'level12_two_actual_period_classes_independent_over_C_proved': True,
    'level12_actual_regular_singular_PV_group_Ga6_semidirect_PSL2_proved': True,
    'level12_six_low_jets_algebraically_independent_over_common_homogeneous_PV_field_proved': True,
    'level12_fixed_two_source_full_Gamma_rational_differential_invariant_field_is_Cv_proved': True,
    'level12_finite_algebraic_covers_preserve_connected_translation_radical_proved': True,
    'level12_affine_Galois_scope': 'Actual two Bol-gauged sources on Gamma and their common homogeneous PV system over C(v), six-jet pure transcendence. Rational differential constructions invariant under full Gamma are in C(v). Not full discrete stabilizer classification, new-source exclusion, or special-value independence; C already contains the numerical constants.',
    'level12_nongauged_actual_primitives_not_Dfinite_over_Cv_proved': True,
    'level12_nongauged_scope': 'Infinite derivative closure for both actual shifted and unshifted primitives, also after finite algebraic base extension. Not infinite rank of an arbitrary finite tuple and not a prohibition on all CDT applications without prior holonomicity.',
    'level12_Jensen_extra_origin_fiber_floor_proved': True,
    'level12_specified_unique_nonnegative_stationary_numerator_same_floor_proved': True,
    'level12_numerator_scope': 'For the stated analytic maps/boundary limits, I(r,1) and J are at least rho+Z_phi. Specified CDT stationary system must have its unique nonnegative solution. Necessary contradiction condition (m-1) mean_rho > m kappa + mean_Z; not an exclusion of all multiple-zero maps or all refinements.',
    'level12_fixed_norm_comparison_does_not_improve_D_squared_term_proved': True,
    'level12_full_affine_holonomy_has_no_fixed_positive_definite_invariant_Hermitian_form_proved': True,
    'level12_new_varying_bundle_arithmetic_holonomy_theorem_proved': False,
    'level12_actual_target_S1_fixed_original_lattice_credit_proved': True,
    'level12_actual_target_S1_gamma': '1/2',
    'level12_actual_target_S1_scope': 'Pure-L native three rows, e=0 and a0=1 fixed original source, stated good-prime prefixes and matching window; not the joint source Up packet.',
    'level12_three_linear_log_characteristic_p_polynomial_zero_estimate_proved': True,
    'level12_fixed_target_S2_lift_background_S3_obstruction_explicit': True,
    'level12_successful_target_S2_or_S3_construction_proved': False,
    'level12_fixed_arrays_cap3_same_matching_window_optimistic_budget_fails': True,
    'level12_cap3_budget_scope': 'Same rank7/13/23 arrays, p<=D theta-matching window, exponents capped at3, ordinary Jensen/plain CDT; excludes neither outside-window nor higher-exponent credit nor separately proved refined numerator floor.',
    'level12_new_mixed_lattice_Smith_credit_proved': False,
    'level12_new_mixed_lattice_Smith_scope': 'No new mixed lattice or higher-layer S2/S3 credit; the proved S1 credit above stays on the fixed original lattice.',
    'mixed_s2_successful_construction_proved': False,
    'complete_cartier_primitive_same_leaf_proved': False,
    'slow_source_polynomial_equation_degree47_proved': True,
    'specified_rank19_unit_budget_complete_but_below_required_margin': True,
    'new_target_integral_extra_smith_gain_proved': False,
    'earlier_goal_turn_before_regulator_stage_classification': 'progress: actual rational CH4 coordinate-symbol family completion exists and is unique nonzero over Q; actual quarter-product rank19 and full Ga8 translation radical, mixed Smith cost10721/722 and J cost188/25; actual conifold D^4 C^n integral-germ model conditional on all three initial jets algebraic. Regulator derivative and compact scalar marking were still open then. No numerical or Lean theorem.',
    'previous_goal_turn_classification': 'progress: actual compact regulator derivative +16 sqrt(x) omega, rational compact rank4 projector and kappa_dR=-1/16; raw positive-cut pairing and Gamma/8 relative-period comparison. Full compact-minus-raw homogeneous marking and three initial-jet arithmetic remained open. No numerical or Lean theorem.',
    'last_goal_turn_classification': 'progress',
    'level12_two_actual_cusp_power_doublecoset_separation_for_all_true_zero_separators_proved': True,
    'level12_same_cusp_distinct_power_doublecosets_separated_proved': True,
    'level12_strict_definite_translation_separates_entire_unknown_kernel_conjugates_proved': True,
    'level12_Gamma_kernel_root_closed_and_odd_even_axis_exception_proved': True,
    'level12_mixed_pair_scope': 'Actual pure-L K=c^-1(0), arbitrary h in K and arbitrary signed integer powers of x4/x5. Two-block separation and strict-definite K-conjugate separation; not all three-or-more block cancellations or a full K classification.',
    'level12_actual_zero_Apery_period_corrector_constructed': True,
    'level12_corrector_all_integer_parameters': 's_n=644n^3+552n^2+147n',
    'level12_corrector_paired_target_germs_and_full_T_Jn_leaves_proved': True,
    'level12_corrector_scope': 'For each fixed integer n, actual F_L+s_n R preserves pure L3(chi12), both coefficient embeddings under the rationality hypothesis, rank4 and safe cubic denominators; the second full Hecke leaf has w_n=sqrt(12)*(84n^2+48n+7). Source has changed, old M leaf is lost for n!=0; no improved common capacity or numerical contradiction claimed.',
    'classic_all_high_odd_zeta_even_derivative_single_value_projection_proved': True,
    'classic_zeta7_actual_nonzero_hypergeometric_forcing_explicit': True,
    'classic_high_odd_projection_all_large_prime_exact_prefix_valuation_proved': True,
    'classic_high_odd_projection_scope': 'For each fixed r>=1, half-integer classical sum of R_n^(2r) is rational plus integer A_n times (2r+2)!*(2^(2r+3)-1)*zeta(2r+3). For r>=2, v_p C_((p+1)/2,r)=-2r at every sufficiently large prime. Prefix denominator growth is between 2r and4r+4; exact safe LCM table D_N^3 D_(2N)^(2r+4). No optimal CDT transport cost, minimum rank, Calabi-Yau geometry, capacity or Archimedean small-form decay claimed.',
    'LSZ_v1_displayed_telescoper_t3_coefficient_repaired_and_original_preserved': True,
    'LSZ_scope': 'Original theorem is 2-adic zeta_2(5), not a classic zeta(5) theorem. Printed inner t3 coefficient768 needs48 under outer16; corrected formal n,t identity is exact. This is not a claim that the main theorem is false.',
    'level12_fixed_log_growth_Hodge_norm_comparison_subleading_proved': True,
    'level12_actual_Bost_scalar_graph_size_summability_fails_proved': True,
    'level12_Hodge_scope': 'Same actual lattice and evaluation, fixed bundle/metric and fixed product dimension before degree limit; not Sym^D or a new arithmetic bundle model. Exact whole-vector grades are separated from the unconstructed primitive scalar pairing.',
    'level12_eisenstein_extension_auxiliary_scope': 'Author auxiliary complete-source/cusp record; peer actual PY/JSON normalization and canonical endpoint review only, root actually read MD/manifest but did not independently audit every boundary slot or execute its producer. No full-MD independent review or numerical theorem is claimed.',
    'classic_actual_fifth_module_is_primitive_exterior_square_of_half_parameter_rank4_proved': True,
    'classic_rank4_connected_monodromy_group_Sp4_proved': True,
    'classic_actual_A_minimal_homogeneous_rank5_proved': True,
    'classic_frobenius_regular_parts_LCM_n_power_j_integral_for_j_le_3_proved': True,
    'classic_spin_geometry_scope': 'Known four-quadrics mirror CY3 module identified with actual project source through the full exterior companion; Levelt GL4Z lattice, Sp4 Lie dimension10 and primitive associative algebra dimension25. Not a new CY family, completed integral comparison, free rank4 replacement of rank5, or special-value theorem.',
    'classic_zeta7_all_hypergeometric_particulars_excluded_proved': True,
    'classic_zeta7_rational_initial_particular_all_prime_band_preserved_proved': True,
    'classic_zeta7_actual_forcing_module_rank5_proved': True,
    'classic_zeta7_actual_forcing_extension_nonsplit_proved': True,
    'classic_zeta7_complete_target_safe_derivative_closure_rank_upper': 10,
    'classic_zeta7_complete_target_minimal_rank_proved': True,
    'classic_zeta7_complete_target_actual_rank': 10,
    'classic_zeta7_complete_target_extension_nonsplit_proved': True,
    'classic_zeta7_all_rational_differential_particulars_in_forcing_module_excluded': True,
    'classic_zeta7_full_rank_scope': 'Actual C2 and all C2+cA over C(x), including the genuine F2. Branch-independent convergent infinity log7/(42x), versus forcing log-degree<=4, plus already proved irreducible K/L5 and nonsplit H inputs. Not the complete PV group or integral comparison.',
    'classic_all_fixed_high_odd_forms_asymptotic_positive_256n_over_n_proved': True,
    'classic_actual_conifold_log_divergence_Abelian_proved': True,
    'classic_actual_A_leading_constant_positive_M1_over_pi4_proved': True,
    'classic_all_fixed_high_odd_actual_Apery_limits_proved': True,
    'classic_canonical_conifold_all_C2_plus_cA_monodromy_nonzero_proved': True,
    'classic_M0_equals_16_critical_weight4_level8_L2_primary_identity_checked': True,
    'classic_connection_scope': 'All fixed r>=1 genuine Apery limits retain pi4*M2r/M1. Exact normalized critical endpoints M0=16L(f8,2), M1=64L(f8,3), M2=4pi2M0 and M3=8pi2M1; M4=56pi4M0-24pi4R0 retains canonical actual forcing boundary. CY wplus=4M1=256L(f8,3) is a Frobenius coordinate comparison, not complete integral Betti calibration. No endpoint identity splits rank5/rank10 functions; canonical conifold obstruction does not classify all transported branches. No new small-form or numerical irrationality theorem.',
    'classic_actual_rank10_common_lambda_filled_cyclic_leaf_proved': True,
    'classic_omit1_unique_simple0_map_class_sharp_derivative_bound': 16,
    'classic_lambda_univalence_radius_exact': 'exp(-pi/2)',
    'classic_lambda_ordinary_J_equals_rho_for_r_le_exp_minus_pi_over2_proved': True,
    'classic_source_and_graded_coordinate_determinant_identity_proved': True,
    'classic_forcing_prefix_safe_LCM_2Nplus1_fourth_power_proved': True,
    'classic_actual_A_dyadic_valuation5_for_all_k_proved': True,
    'classic_levelt_primitive_saturated_rank5_and_quotient_index8_proved': True,
    'classic_lambda_arithmetic_scope': 'Same actual germs and original rational-variable rank10; omit1/unique simple0 class only. Original z=x/256 capacity<=1/16. Fixed prime2 coordinate changes can contribute the evaluation D2 leading term. Forcing denominator rate between4 and8, A_(2^k) valuation5, explicit primitive index8. No complete F2 optimal/mixed arithmetic fee or Taylor/deRham integral comparison is claimed.',
    'level12_integer_corrector_actual_mirror_augmented_leaves_proved': True,
    'level12_complete_R_nine_generator_cocycle_integer_lattice_proved': True,
    'level12_corrector_two_new_pure_L_sources': ['-311/6', '-419/6'],
    'level12_corrector_two_new_sources_integral_q_coefficients_proved': True,
    'level12_all_eligible_chi_minus_reflection_mirror_pair_radius_baseline_maximal_proved': True,
    'level12_all_fixed_rational_corrector_componentwise_three_layers_proved': True,
    'level12_general_pair_scope': 'Only complete zero-identity corrected sources and their fixed reflection/real-mirror pair disks; exact Green wordwise comparison and ordinary-J fixed arrays. Does not bound larger zero groups, other sources/maps, mixed Smith lattices, or all bundle/refined metrics.',
    'level12_complete_cuspidal_basis_dimension7_proved': True,
    'level12_cuspidal_fricke_minus_dimension3_proved': True,
    'level12_three_actual_integral_cusp_corrector_sources_constructed': True,
    'level12_cusp_actual_L3_positive_and_ratio_interval_proved': True,
    'level12_cusp_ratio_interval': ['3*sqrt(3)', '4+sqrt(3)'],
    'level12_cusp_pure_period_and_extra_reflection_endpoint_conditions_explicit': True,
    'level12_new_K_zero_critical_cusp_period_relation_proved': False,
    'level12_cuspidal_third_independent_zero_generator_constructed': False,
    'level12_cusp_scope': 'Full S4 of the actual genus0 ten-cusp Gamma and its W-minus basis U,X0,X2. Nonzero positive L3 and strict real ratio bound do not establish K independence or a K kernel. Genuine conjugate-source additive endpoints, not Galois actions on unknown numerical periods. Two-block eta^n T^m reflected family has the stated all-integer restriction, not full-kernel classification.',
    'classical_M1_exact_L_f8_3_multiplier': 64,
    'classical_M2_exact_four_pi2_M0_proved': True,
    'classical_M3_exact_eight_pi2_M1_proved': True,
    'classical_bilateral_entire_three_modes_and_half_period_identity_proved': True,
    'classical_M4_exact_56pi4_M0_minus24pi4_R0_proved': True,
    'classical_R0_actual_H_fourth_boundary_calibrated': True,
    'classical_T_quarter_shift_critical_projection_proved': True,
    'classical_M4_actual_rank5_and_nonsplit_proved': True,
    'classical_H_fullprefix_mod_p2_packet_proved': True,
    'classical_H_original_rank10_smith_thresholds8_9_proved': True,
    'classical_original_near_balanced_smith_gamma': '11/3',
    'classical_specified_full_safe_array_CDT_cost_credit': '11/150',
    'classical_full_F_high_layer_smith_credit_proved': True,
    'classical_M4_integral_regulator_comparison_proved': False,
    'level12_actual_Manin_critical_and_endpoint_period_matrix_proved': True,
    'level12_two_chi_cusp_source_double_zero_obstruction_proved': True,
    'level12_full_three_cusp_source_zero_kernel_classified': False,
    'quarter_shift_actual_rank5_nonsplit_proved': True,
    'quarter_shift_exact_allprime_prefix_denominator_proved': True,
    'classical_H_exact_prefix_denominator_proved': True,
    'quarter_shift_same_source_split_smith_credit': '4/25',
    'quarter_shift_ordinary_certified_cost_upper_bound': '188/25',
    'quarter_shift_optimal_cost_proved': False,
    'R0_actual_B_H_contiguity_proved': True,
    'R0_Kummer_extension_distinct_from_Z4_proved': True,
    'R0_full_conifold_log_projection_proved': True,
    'R0_geometric_normal_function_or_regulator_comparison_proved': True,
    'R0_geometric_normal_function_scope': 'Specified rational Chow AJ family, actual derivative, and explicit centered current compact lift with scalar -16(2pii)^3 W. Actual Gamma/8 rational compact Tate correction gives -16(2pii)^3 Psi. This selected marking and the actual compact rank-four saturated integral sector are proved; arbitrary old membranes still differ by rational compact periods. No integral Chow completion or numerical theorem.',
    'level12_three_source_actual_U_endpoint_proved': True,
    'level12_three_source_specified_double_zero_iff_proved': True,
    'level12_three_source_actual_numeric_ratios_decided': False,
    'ehmm_actual_period_product_projection_proved': True,
    'ehmm_full_source_integral_comparison_proved': False,
    'classical_full_F_odd_all_prime_power_safe_positive_columns': 8,
    'classical_full_F_actual_whole_prefix_mod_p2_packet_proved': True,
    'classical_full_F_original_rank10_new_floor_baseline': 24,
    'classical_full_F_high_layer_gamma': '5/2',
    'classical_full_H_F_original_rank10_total_gamma': '37/6',
    'classical_full_H_F_ordinary_safe_cost_upper_bound': '3239/300',
    'classical_full_H_F_ordinary_cost_is_proved_optimal': False,
    'complementary_quarter_actual_Gamma_free_period_product_proved': True,
    'complementary_quarter_scalar_prefix_exact_denominator_rate': 16,
    'complementary_quarter_rational_derivative_model_rank_upper_bound': 19,
    'complementary_quarter_actual_minimal_rank19_proved': True,
    'complementary_quarter_actual_joint_translation_radical_dimension': 8,
    'complementary_quarter_actual_minimal_rank19_preserved_on_finite_algebraic_covers': True,
    'complementary_quarter_mixed_whole_prefix_primitive_Smith_proved': True,
    'complementary_quarter_exact_allprime_prefix_denominator_product': 'odd(D_(4N+1))^4',
    'complementary_quarter_original_rank19_mixed_gamma': '31/4',
    'complementary_quarter_original_rank19_ordinary_certified_cost_upper_bound': '10721/722',
    'complementary_quarter_original_rank19_cost_is_proved_optimal': False,
    'complementary_quarter_all_arithmetic_initial_homogeneous_Sym2_constant_corrections_obstructed': True,
    'R0_finite_algebraic_coefficient_linear_period_retaining_conifold_correction_obstructed': True,
    'R0_actual_integral_relative_cube_minus_tube_marking_proved': True,
    'R0_actual_relative_marking_conifold_period': '8*pi^2*(R0-M0)',
    'R0_actual_four_quadrics_mirror_generic_quotient_degree': 64,
    'R0_actual_mirror_native_parameter': '1/x',
    'R0_all_divisorial_coordinate_Milnor_symbol_tame_residues_rationally_zero_proved': True,
    'R0_toric_model_regular_for_Doran_Kerr_theorem3_1': False,
    'R0_higher_Chow_lift_and_d2_completion_proved': True,
    'R0_higher_Chow_lift_scope': 'Rational CH4(Y,4) coordinate-symbol class on a resolved proper smooth four-dimensional family over Gm/Q; actual split horizontal strata and all d_r targets. Smooth fibres lambda!=256 only. Not explicit boundary precycles, regulator-current marking comparison, or integral saturation.',
    'R0_boundary_CH0_E_degree4_rationally_zero_proved': True,
    'R0_family_coordinate_symbol_Chow_completion_rationally_unique_proved': True,
    'R0_family_coordinate_symbol_Chow_class_nonzero_proved': True,
    'R0_family_completion_uniqueness_scope': 'CH4(Y,4)_Q family class over Q, via actual global split rational-puncture strata, number-field K4 and CH2(Q,3) vanishing, and two singular CH0 localization steps. Generic four vertical tame residues certify nonzero. Not integral torsion, cycle representatives, base change to C/Q(x), individual fibre completion uniqueness, or Betti/current lift uniqueness.',
    'R0_conifold_geometric_order5_conditional_integral_germ_proved': True,
    'R0_conifold_arithmetic_germ_required_initial_data': ['alpha0', 'alpha1', 'alpha2'],
    'R0_conifold_three_initial_jets_all_algebraic_proved': False,
    'R0_conifold_geometric_conditional_prefix_model': 'Historical unspecified-C model d0*D_(N+b0+3)^4*C^(N+4), now superseded for normalized g/h and paired packet by explicit dyadic/odd bounds with polynomial small-prime factors; algebraicity of all three actual Psi jets remains unproved.',
    'R0_conifold_finite_bad_prime_C_effective_or_optimal_proved': True,
    'R0_conifold_finite_bad_prime_C_optimal_proved': False,
    'R0_conifold_germ_is_regular_ordinary_point': False,
    'R0_complete_compact_integral_sector_saturation_proved': True,
    'R0_full_relative_Betti_conifold_monodromy_invariant_proved': False,
    'R0_compact_regulator_top_form_extension_proved': True,
    'R0_compact_regulator_GaussManin_derivative_proved': True,
    'R0_compact_regulator_GaussManin_derivative': '+16*sqrt(x)*omega_x',
    'R0_compact_regulator_derivative_scope': 'Rational real-admissible KLM complex, local BM membrane and prescribed-fibre pullback; ordinary compact H3 cohomology and LEFT residue. Frozen unproved negative candidate corrected in a NEW proof. No automatic DK ell2,3 application.',
    'R0_compact_H3_and_AJ_open_restriction_injective_over_Q_proved': True,
    'R0_actual_regulator_family_nonflat_proved': True,
    'R0_actual_regulator_AJ_very_general_nonzero_proved': True,
    'R0_actual_regulator_AJ_at_specified_algebraic_parameter_nonzero_proved': False,
    'R0_actual_rank4_compact_rational_projector_proved': True,
    'R0_actual_rank4_compact_rational_projector_scope': 'Actual degree-one common graph resolution, compact mirror full cohomological PF and cyclic rank4. Pullback and PD pushforward act on free integer H3, qi=id_Q upgrades to qi=id_Z; actual horizontal orthogonal projector is integral and sector saturated unimodular. Does not identify all open/compact H3 with rank4.',
    'R0_actual_cyclic_cup_matrix_proved': True,
    'R0_actual_Yukawa_kappa_raw': '-(2*pi*i)^3/16',
    'R0_actual_Yukawa_kappa_dR': '-1/16',
    'R0_actual_Gamma_vanishing_cycle_intersection': -8,
    'R0_actual_Yukawa_scope': 'Independent real node sphere, true compact Gamma, anticlockwise PL total dimension4 and full scalar concomitant; fixed LEFT residue and raw cup order. Not inferred from the raw KLM integral.',
    'R0_compact_scalar_actual_inhomogeneous_PF_proved': True,
    'R0_compact_scalar_actual_inhomogeneous_PF': 'P4*nu_raw=-(2*pi*i)^3*sqrt(x)',
    'R0_raw_positive_cut_each_sheet_absolute_convergence_proved': True,
    'R0_raw_positive_cut_each_sheet_finite_conifold_boundary_limit_proved': True,
    'R0_raw_positive_cut_pairing_proved': True,
    'R0_raw_positive_cut_pairing': 'nu_cut=-16*(2*pi*i)^3*W',
    'R0_actual_Gamma_over8_analytic_Tate_period_correction_proved': True,
    'R0_positive_cut_comparison_scope': 'Exact raw integral and all-corner centered-current compact extension proved; centering has explicit flat rational OPEN Q(4) correction, but leaves raw scalar unchanged by absolutely convergent opposite sheets. Actual centered compact AJ lift and actual Gamma/8 chosen marking identify nu_corr. The integer Betti sector and selected cocycle are now proved; literal raw cubical compact graph and integer higher-Chow completion are not asserted.',
    'R0_actual_completed_current_matches_raw_scalar_lift_proved': True,
    'R0_actual_scalar_homogeneous_discrepancy_determined': True,
    'R0_actual_scalar_homogeneous_discrepancy_scope': 'Explicit centered-current plus actual Gamma/8 chosen lift only; not a universal marking of every earlier membrane or vanishing-normalized real lift.',
    'R0_conifold_special_value_marked_actual_regulator_proved': True,
    'current_round_new_mathematical_producer_runs': 3,
    'current_round_new_mathematical_producer_run_scope': 'Own root exact Fraction recurrence probe degree180 once and own new symbolic verifier13 checks once; quarter own new integral-matrix verifier38 checks once. No old/peer mathematical producer execution or import. All-n geometry, denominators and holonomy results rest on paper proofs.',
    'R0_positive_cut_actual_open_regulator_class_proved': True,
    'R0_positive_cut_actual_flat_rational_open_Tate_discrepancy_proved': True,
    'R0_positive_cut_actual_open_discrepancy_compactness_boundary_condition_proved': True,
    'R0_positive_cut_relative_boundary_in_H2_E_zero_proved': False,
    'R0_full_compact_H3_restriction_to_singular_boundary_zero_proved': True,
    'R0_full_compact_H3_support_lift_surjective_proved': True,
    'R0_compact_support_kernel': 'coker(H2(X,Q)->H2(E,Q))',
    'R0_local_specified_rational_horizontal_support_trace_proved': True,
    'R0_canonical_relative_form_equals_specified_horizontal_support_lift_proved': False,
    'R0_actual_boundary_Stokes_flux_and_relative_trace_identity_proved': True,
    'R0_boundary_flux_zero_proved': True,
    'R0_boundary_flux_zero_scope': 'Canonical relative (omega,0) only, proved by all-corner angular coarea and smooth relative primitive vanishing on every SNC component. Arbitrary rational horizontal support splitting flux is not proved zero.',
    'R0_full_four_jet_Gamma_over8_scalar_marking_conditions_explicit': True,
    'R0_actual_local_vanishing_symbol_regulator_evaluation_proved': True,
    'R0_actual_vanishing_regulator_period': 'Adelta=16*pi2*integral_0^t(v(s)/sqrt(1-s))ds',
    'R0_actual_vanishing_regulator_integer_Tate_constant_proved': True,
    'R0_actual_vanishing_regulator_concomitant_identity': 'Adelta=256*C0(W,g)+(2*pi*i)^4',
    'R0_Gamma_over8_actual_canonical_vanishing_evaluation_alignment_proved': True,
    'R0_actual_compact_scalar_vanishing_normalized_conifold_holomorphic_lift_proved': True,
    'R0_actual_scalar_discrepancy_after_vanishing_normalization_dimension': 3,
    'R0_remaining_three_holomorphic_scalar_coefficients_determined': False,
    'R0_single_endpoint_dual_arithmetic_germ_proved': True,
    'R0_single_endpoint_dual_arithmetic_germ_required_data': ['alpha0'],
    'R0_single_endpoint_dual_minimal_scalar_order': 5,
    'R0_single_endpoint_dual_complete_rank_with_constant_one': 6,
    'R0_single_endpoint_dual_complete_prefix_model': '16*d0*D_(N+b0+3)^4*(4*Cg)^(N+4)',
    'R0_actual_Tate_vanishing_shift_preserves_endpoint_and_delta_normalization_but_changes_transcendental_first_jet_proved': True,
    'R0_constant_translation_blindness_of_isolated_dual_branch_data_proved': True,
    'R0_new_endpoint_sensitive_second_Betti_relation_proved': True,
    'R0_original_open_Tate_discrepancy_actual_noncompact_proved': True,
    'R0_original_open_Tate_bounding_torus_period': '-1',
    'R0_raw_positive_current_bounding_torus_period': '(2*pi*i)^4',
    'R0_centered_current_all_surviving_cones_uniform_angular_coarea_proved': True,
    'R0_centered_current_all_corner_common_forced_minus_one_factor_proved': True,
    'R0_centered_current_locally_integrable_compact_zero_extension_proved': True,
    'R0_centered_current_total_derivative_has_no_boundary_residual_proved': True,
    'R0_centered_current_actual_marked_compact_AJ_scalar_proved': True,
    'R0_centered_current_selected_three_homogeneous_comparison_coefficients_determined': True,
    'R0_arbitrary_real_delta_lift_three_coefficients_determined': False,
    'R0_real_compatible_compact_AJ_average_proved': True,
    'R0_real_Betti_plus_minus_dimensions': [2, 2],
    'R0_real_delta_compatible_rational_shift_dimension': 1,
    'R0_actual_remaining_real_cycle': '-(M0-M0_inverse)*delta-2*Gamma',
    'R0_physical_origin_monodromy_trace': -4,
    'R0_signed_period_origin_transport': 'U0=-M0',
    'R0_actual_delta_physical_M0_delta_intersection': -8,
    'R0_remaining_real_cycle_strict_positive_endpoint_proved': True,
    'R0_remaining_real_cycle_endpoint_lower_bound': '16*pi2*log(2)^2+pi4/3',
    'R0_remaining_real_cycle_origin_log2_coefficient': 'pi2/4',
    'R0_endpoint_sensitive_exterior_actual_Galois_translation_dimension': 4,
    'R0_endpoint_sensitive_exterior_actual_rank': 9,
    'R0_endpoint_sensitive_exterior_complete_rank_with_one': 10,
    'R0_endpoint_sensitive_exterior_scalar_minimal_order': 9,
    'R0_endpoint_sensitive_exterior_original_pure_prefix_LCM_power': 10,
    'R0_endpoint_sensitive_exterior_contracted_pure_prefix_LCM_power': 7,
    'R0_endpoint_sensitive_exterior_mixed_prefix_LCM_power': 6,
    'R0_endpoint_sensitive_exterior_safe_complete_prefix': '16*d0*D_(N+b0+3)^7*C^(N+12)',
    'R0_endpoint_sensitive_exterior_arithmetic_hypothesis': 'alpha0 in a number field; not equivalent to R0-M0 rational or algebraic',
    'R0_endpoint_sensitive_exterior_highest_log_relation': 'N0^3*p_plus*Phi(q)=0 iff q=alpha0',
    'R0_endpoint_sensitive_exterior_flag_is_proved_CDT_capacity_improvement': False,
    'R0_endpoint_sensitive_exterior_actual_value_sensitive_filled_word_constructed': False,
    'R0_endpoint_sensitive_exterior_paired_conifold_filled_branch_data_constant_blind_proved': True,
    'R0_endpoint_sensitive_exterior_infinity_Jordan_size': 5,
    'R0_endpoint_sensitive_exterior_all_infinity_branches_unfillable_on_finite_covers_proved': True,
    'R0_actual_compact_integer_orthogonal_projector_proved': True,
    'R0_actual_compact_sector_free_integer_lattice_unimodular_proved': True,
    'R0_actual_vanishing_orbit_index_in_saturated_sector': 256,
    'R0_actual_vanishing_orbit_intersection_Smith': [8,8,32,32],
    'R0_actual_vanishing_orbit_inclusion_Smith_complete_proved': False,
    'R0_selected_compact_regulator_integer_Betti_cocycle_proved': True,
    'R0_actual_origin_spectral_and_highest_log_operators_integer_proved': True,
    'R0_canonical_Taylor_to_Betti_arithmetic_comparison_proved': False,
    'R0_integer_higher_Chow_completion_proved': False,
    'R0_normalized_conifold_all_n_dyadic_denominator_proved': True,
    'R0_normalized_conifold_dyadic_bound': 'b(n)=2n+2v2(n!)-floor(n/2)<=7n/2, for g0,g1,g2,h',
    'R0_fixed_toric_model_projective_smooth_all_odd_primes_proved': True,
    'R0_fixed_toric_model_split_relative_SNC_all_odd_primes_proved': True,
    'R0_integral_deRham_crystalline_torsion_free_proved': False,
    'R0_actual_G4_G5_generic_radius_one_all_odd_primes_proved': True,
    'R0_all_odd_generic_radius_scope': 'Proper smooth all-odd X, rational convergent crystalline realization, NEW relative PD/Cech/GM comparison, actual cohomological cyclic sector/dual and odd etale sqrt twist; rational generic-disk gauges preserve radius. G5 independently uses determinant and variation of constants, not an integral motivic Frobenius assertion.',
    'R0_normalized_g_all_prime_denominator': '2^b(n)*odd(D_n)^3*3^(2floorlog3(n))',
    'R0_normalized_h_all_prime_denominator': '2^b(n)*odd(D_n)^4*3^floorlog3(n)*5^(4floorlog5(n))',
    'R0_paired_nine_row_explicit_rational_C': 16,
    'R0_paired_nine_row_complete_number_field_scale_proved': True,
    'R0_paired_nine_row_number_field_scale': 'L=K(sqrt2), a=8sqrt2; every2-place v2(a)=7/2, all odd a-unit, all embeddings |sigma(a)|=2^(7/2)',
    'R0_paired_nine_row_number_field_scale_log_cost': '(7/2)*log2',
    'R0_paired_nine_row_number_field_scale_savings_over_log16': '(1/2)*log2',
    'R0_paired_number_field_scale_scope': 'Complete all-place coefficient clearing, strict polynomial and epsilon species retained, all conjugate parameters/maps checked, normalized field-degree costs and rank10 unchanged; conditional product-formula optimum only for scales required to clear the existing uniform dyadic upper bound, no actual optimal denominator claim.',
    'R0_paired_nine_row_strict_prefix_denominator': '2^25*d0*16^N*P3(N)*D_(N+6)^sigma, sigma=7 for four Z and6 for five mixed; P3(N)=3^(4floorlog3(N+6)); every0<=n<=N, all finite places',
    'R0_paired_nine_row_small_prime_polynomial_factor_retained': True,
    'R0_CDT_small_prime_polynomial_o_D2_and_literal_epsilon_species_proved': True,
    'R0_CDT_exact_ten_row_species_tau': '329/50',
    'R0_canonical_origin_finite_cover_linear_differential_meromorphic_projection_no_go_proved': True,
    'R0_canonical_origin_no_go_scope': 'Actual nine-dimensional packet, algebraic scalar rows and fixed rational linear differential operators, finite algebraic covers; nonzero primitive quotient jump forces full evaluation kernel. Does not exclude new transported words, nonlinear packets or a new vector-valued holonomy theorem.',
    'R0_common_q_domain_rank10_q0_reference_obstruction_proved': True,
    'R0_value_sensitive_meromorphic_domain_or_capacity_contradiction_proved': False,
    'current_round_new_mathematical_proof_and_review_files': len(proofs)-93,
    'current_round_new_frozen_mathematical_inputs': len(current_frozen)-265,
    'current_round_new_source_receipts': 5,
    'current_round_new_primary_pdf_files': 3,
    'current_round_new_primary_pdf_pages': 57,
    'current_round_newly_registered_existing_primary_pdf_files': 1,
    'current_round_newly_registered_existing_primary_pdf_pages': 20,
    'current_round_newly_registered_existing_primary_pdf': 'literature/cdt2025_arithmetic_holonomy.pdf',
    'last_goal_turn_mathematical_progress': 'Actual integer orthogonal projector and saturated unimodular sector; exact real vanishing orbit index256, integer selected regulator cocycles and actual origin flags. All-n dyadic bound b(n)<=3.5n, all-odd smooth fixed-fan family, rational crystalline/relative deRham comparison giving actual G4/G5 generic radius1, complete C16 paired prefix with strict p3 polynomial and literal epsilon-species tau329/50. Separate complete L=K(sqrt2), a=8sqrt2 model reduces both arch scale costs to3.5log2 with all finite places and all embeddings charged, rank10 unchanged. Canonical-origin finite-cover linear no-go and genuine rank10 q0 common-domain obstruction remain. Actual Taylor/Betti arithmetic comparison and value-sensitive analytic domain or new full packet remain unresolved. No numerical odd-zeta/L/Catalan or Lean theorem.',
    'current_round_scope': 'NEW paper proofs and independent reviews with exact final source/read-scope pins; three own new mathematical producer runs only (root2, quarter1), no old/peer execution/import/rerun. Three new verified-TLS primary PDFs Katz35, Morrow12, Bhatt-deJong10, five source receipts. Relative crystalline comparison is explicitly proved rather than attributed verbatim to the printed absolute theorem. Root all-n dyadic proof independently reviewed by quarter. Betti B11 parameter-family error corrected before freeze after independent discovery; all initial/final versions disclosed. All345 previous frozen inputs preserved. Mutable delivery audit verifies hashes, certificates, primary metadata and local links only. Project internal paper proofs/review, no published numerical result or Lean.',
}
out.update({
    'current_round_new_mathematical_producer_runs': 3,
    'current_round_new_mathematical_producer_run_scope': 'Root three NEW standalone producers each first execution once: original-layout exact residue LP, restored-layout exact residue LP, standalone integration/weight/log/atan certificate checker. No old/peer producer execution, import or rerun; no external Lean compilation or execution. Quarter actual full static reads, no independent code execution claimed.',
    'current_round_previous_frozen_mathematical_inputs': 376,
    'current_round_new_mathematical_proof_and_review_files': len(proofs)-118,
    'current_round_new_frozen_mathematical_inputs': len(current_frozen)-296,
    'current_round_new_source_receipts': 4,
    'current_round_new_source_receipt_pins': [
        {'file': 'literature/' + name, 'sha256': manifest_pins[name], 'file_hash_checked': True}
        for name in [
            'manifest_cdt_odd_mixed_double_pole_arithmetic_cost_20261006.json',
            'manifest_cdt_odd_mixed_double_pole_analytic_decay_20261006.json',
            'manifest_cdt_odd_mixed_double_pole_primitive_lattice_20261006.json',
            'manifest_cdt_odd_double_pole_layout_budget_root_20261006.json',
        ]
    ],
    'current_round_new_primary_pdf_files': 0,
    'current_round_new_primary_pdf_pages': 0,
    'current_round_newly_registered_existing_primary_pdf_files': 0,
    'current_round_newly_registered_existing_primary_pdf_pages': 0,
    'current_round_newly_registered_existing_primary_pdf': None,
    'current_round_new_primary_repository_source_files': 0,
    'current_round_new_primary_repository_source_bytes': 0,
    'current_round_external_lean_compilation_and_execution': 0,
    'current_round_complete_external_kernel_proof_revalidation': False,
    'R0_actual_all_word_origin_mod8_obstruction_proved': True,
    'R0_all_word_origin_mod8_obstruction_scope': 'Actual monodromy subgroup preserves the vanishing-cycle orbit lattice; signed ell-orbit is1 mod8, physical is+/-1. Not every integral Sp4 transformation; no rational-Betti-plane assumption.',
    'R0_all_transported_origin_finite_cover_meromorphic_no_go_proved': True,
    'R0_actual_decomposable_connected_stabilizer_dimension': 8,
    'R0_actual_decomposable_orbit_dimension': 6,
    'R0_rational_differential_output_origin_and_infinity_q_blindness_proved': True,
    'R0_fixed_q_free_rational_output_holomorphic_disk_common_domain_proved': True,
    'R0_fixed_q_free_rational_output_differential_rank_parameter_independent_proved': True,
    'R0_finite_algebraic_root_ordinary_discriminant_branching_excluded': False,
    'R0_nonlinear_budget_inherited_from_original_nine_rows': False,
    'R0_full_jump_Cauchy_positive_part_evaluation_reduction_proved': True,
    'R0_full_jump_uniform_degree_exponential_suppression_proved': False,
    'R0_endpoint_row_projective_K_descent_criterion_proved': True,
    'R0_endpoint_row_actual_projective_K_descent_proved': False,
    'mixed_zeta_higher_logistic_exact_target_moment_identity_proved': True,
    'mixed_character_Hurwitz_trace_exact_target_identity_proved': True,
    'mixed_character_multicontour_energy_proved': False,
    'mixed_double_pole_all_fixed_s_ge4_auxiliary_prime_nonvanishing_proved': True,
    'mixed_double_pole_auxiliary_prime_block': '(s-2)!*b*W*[[ -(s+1), s ],[ s, -(s-1) ]]; determinant= -((s-2)!*b*W)^2; p=9m+1>max(s,abs(b)), n=2m, whole-form scale p^(s-4).',
    'mixed_double_pole_new_weight_all_prime_cost_and_strict_margin_proved': False,
    'mixed_double_pole_all_finite_place_entire_polynomial_Gauss_content_model_proved': True,
    'mixed_double_pole_original_s5_right_contour_head_correction_exact_rank': '2n',
    'mixed_double_pole_original_complete_analytic_decay_safe_exponent': '9*log(3)',
    'mixed_double_pole_restored_zero_general_layout_nonzero_proved': True,
    'mixed_double_pole_restored_zero_general_analytic_tangent_exponent_proved': True,
    'mixed_double_pole_auxiliary_prime_actual_factorial_fee_retained': True,
    'mixed_double_pole_original_residue_bound_model_weight_penalty': '63/4 per added weight; not actual arithmetic-cost lower bound',
    'mixed_double_pole_restored_s5_bound_comparison': [
        {'B':5,'rank':'n','arithmetic_A_strict_safe_upper':'17.834','analytic_beta_strict_window':['7.642','7.643']},
        {'B':6,'rank':'2n','arithmetic_A_strict_safe_upper':'35.939','analytic_beta_strict_window':['17.476','17.477']},
        {'B':8,'rank':'4n','arithmetic_A_strict_safe_upper':'81.249','analytic_beta_strict_window':['43.029','43.030']},
    ],
    'mixed_double_pole_matched_strict_positive_margin_proved': False,
    'mixed_double_pole_paired_head_free_subspace_dimension': '2n',
    'mixed_double_pole_paired_subspace_saturated_lattice_budget_and_nonzero_proved': False,
    'R0_canonical_origin_no_go_scope': 'Upgraded to all actual transported origin branches and specified rational differential/tensor/projective operations. Finite algebraic roots retain ordinary discriminant branching scope; independent periods, new jump-holonomy theorems and nonalgebraic transforms remain outside.',
    'last_goal_turn_mathematical_progress': 'All finite-place Gauss/common-content model for entire mixed-zeta target polynomials, exact auxiliary-prime Smith/index/factorial fees and primitive constant reduction. Actual s5 triple-zero right-contour correction has rank2n; complete left-contour decay9log3 is proved. General zero-order s-1 layouts restore right contours and retain infinite nonzero subsequences, with exact uniform G and tangent beta. Continuous residue-minor model integrated exactly: original-layout weight penalty63/4, restored s5 B5/B6/B8 safe arithmetic upper bounds17.834/35.939/81.249 against beta windows7.642-7.643/17.476-17.477/43.029-43.030. Current bounds do not prove positive margin and are not actual-cost lower bounds. Paired dimension2n head-free rational subspace constructed with saturation/basis/nonzero unpaid. No new numerical odd-zeta/L/Catalan theorem or Lean proof.',
    'current_round_scope': 'Four NEW mathematical papers, four actual independent peer/root review files, three own NEW standalone producer/certificate pairs, four immutable source receipts. Previous376 mathematical pins unchanged. Root producer runs3, each first execution once; old/peer execution/import/rerun0, agents own producer0, externalLean0. No new or newly registered PDF/repository code. Existing Lai archive actual root13 pages this round/cumulative20, arithmetic25, toric16, quarter14; no shared reading counted as root full verification. Independent review corrected R4 Bn range typo and raw-row primitive naming before freeze. Quarter late full read of root receipt separately recorded in main. File audit only reads hashes, certificates, primary metadata and links.',
})
out.update({
    'current_round_previous_frozen_mathematical_inputs': 390,
    'current_round_new_frozen_mathematical_inputs': len(current_frozen)-310,
    'current_round_new_mathematical_proof_and_review_files': len(proofs)-126,
    'current_round_new_mathematical_producer_runs': 2,
    'current_round_root_own_mathematical_producer_runs': 0,
    'current_round_agents_own_mathematical_producer_runs': 2,
    'current_round_new_mathematical_producer_run_scope': 'Two peer authors each created and first-ran their own NEW standalone program once: toric exact rational logarithmic constants18checks; arithmetic actual paired p8 constraint/Gram/Smith probe10cases at five auxiliary primes. Root ran no mathematical producer. Every independent reviewer read peer code/certificates only, no peer execution/import/rerun, externalLean0.',
    'current_round_old_or_peer_mathematical_producer_execute_import_rerun': 0,
    'current_round_new_source_receipts': 4,
    'current_round_new_source_receipt_pins': [
        {'file': 'literature/' + name, 'sha256': manifest_pins[name], 'file_hash_checked': True}
        for name in [
            'manifest_cdt_odd_paired_head_free_integral_lattice_20261006.json',
            'manifest_cdt_odd_paired_head_free_auxiliary_prime_20261006.json',
            'manifest_cdt_odd_restored_zero_equilibrium_energy_20261006.json',
            'manifest_cdt_odd_paired_analytic_equilibrium_root_20261006.json',
        ]
    ],
    'current_round_new_primary_pdf_files': 3,
    'current_round_new_primary_pdf_pages': 82,
    'current_round_root_actual_primary_pdf_pages_read': 28,
    'current_round_primary_pdf_reading_scope': 'Root Brown14 actualpages1-10/21-24, Saff5 actualpages32-36, Monien6 actualpages1-6, existingLai3 actualpages23-25; Lai cumulative22 actualpages1-14/18-25, not full25. Quarter own analyticreview Brown8+Monien3, toric Saff5, arithmetic equilibriumreview Saff5; distinct persons are not added to root full reading. New PDF archive82pages is not full proof revalidation.',
    'current_round_newly_registered_existing_primary_pdf_files': 0,
    'current_round_newly_registered_existing_primary_pdf_pages': 0,
    'current_round_newly_registered_existing_primary_pdf': None,
    'current_round_new_primary_repository_source_files': 0,
    'current_round_new_primary_repository_source_bytes': 0,
    'current_round_external_lean_compilation_and_execution': 0,
    'current_round_complete_external_kernel_proof_revalidation': False,
    'mixed_double_pole_restored_zero_actual_equilibrium_measure_proved': True,
    'mixed_double_pole_restored_zero_equilibrium_support_radius_squared': '(B-4)*(B+8)/8, s5,k4, fixed right line',
    'mixed_double_pole_restored_zero_all_n_equilibrium_upper_bound_proved': True,
    'mixed_double_pole_restored_zero_fixed_positive_envelope_exact_n2_energy_limit_proved': True,
    'mixed_double_pole_restored_zero_actual_complex_determinant_optimality_or_no_go_proved': False,
    'mixed_double_pole_restored_s5_equilibrium_comparison': [
        {'B':5,'rank':'n','arithmetic_A_strict_safe_upper':'17.834','analytic_beta_strict_window':['8.108','8.109'],'strict_gain_over_old_tangent_upper_at_least':'0.465'},
        {'B':6,'rank':'2n','arithmetic_A_strict_safe_upper':'35.939','analytic_beta_strict_window':['18.276','18.277'],'strict_gain_over_old_tangent_upper_at_least':'0.799'},
        {'B':8,'rank':'4n','arithmetic_A_strict_safe_upper':'81.249','analytic_beta_strict_window':['46.406','46.407'],'strict_gain_over_old_tangent_upper_at_least':'3.376'},
    ],
    'mixed_double_pole_paired_head_free_saturated_integer_basis_proved': True,
    'mixed_double_pole_paired_head_free_exact_raw_index_and_norm_fees_proved': True,
    'mixed_double_pole_paired_head_free_all_finite_place_safe_minor_bridge_proved': True,
    'mixed_double_pole_paired_head_free_factorial_minor_fee': '2*sum_{i=n}^{3n-1}vp(i!), largest2n, original degree<3n retained',
    'mixed_double_pole_paired_head_free_actual_auxiliary_prime_negative_evaluation_rank': '5m/2, n2m,p9m+1 prime,m even; kernel3m/2',
    'mixed_double_pole_paired_head_free_actual_first_jet_and_two_matrix_criterion_proved': True,
    'mixed_double_pole_paired_head_free_auxiliary_prime_conditional_smith': '(-s)^(5m/2),(-(s-2))^(3m/2) and Gauss -m(4s-3), only when detG0 and detMs are both units',
    'mixed_double_pole_paired_head_free_auxiliary_prime_infinite_two_unit_condition_proved': False,
    'mixed_double_pole_paired_head_free_infinite_nonzero_proved': False,
    'mixed_double_pole_paired_head_free_actual_right_contour_and_weighted_plucker_bound_proved': True,
    'mixed_double_pole_paired_head_free_actual_analytic_n2_rate_proved': False,
    'mixed_double_pole_paired_head_free_complete_cheap_gauss_n2_budget_proved': False,
    'mixed_double_pole_matched_strict_positive_margin_proved': False,
    'last_goal_turn_mathematical_progress': 'Explicit one-charge positive mixture yields restored s5,k4 equilibrium support(B-4)(B+8)/8, a fully charged all-n determinant upper bound, closed beta and exact fixed positive-envelope n2 threshold. B5/6/8 beta windows8.108-8.109/18.276-18.277/46.406-46.407 improve old tangents but stay below current safeA. Original paired head-free space has an explicit complete saturated integer basis, exact raw index and Newton-norm fees, all-finite safe common-minor bridge with largest2n factorial costs, exact negative evaluation rank5m/2, actual shared half-jet lift, and conditional two-matrix Smith/Gauss constant-reduction criterion. Infinite unit/nonzero remains open despite10finite exactcases. Same paired determinant now has true generalized Vandermonde, total-variation Gram and weighted Plucker analytic bounds; no borrowed k4 rate. No new numerical odd-zeta/L/Catalan theorem or Lean.',
    'current_round_scope': 'Four NEW mathematical papers with actual independent root and cross reviews, two peer-author NEW first-execution-only producer/certificate pairs, four final immutable source receipts. All previous390 mathematical pins preserved. Root mathruns0, authors own2, every reviewer peer/old execute/import/rerun0, externalLean0. Three default verified-TLS primary PDFs34+36+12=82archivepages, no repository source added. Actual PDF reading scopes disclosed by person. Lattice LP domain p<=6n and auxiliary source/parameter clarifications corrected before freeze. Fixed-envelope exact energy is not an actual complex determinant lower bound; paired two-unit criterion remains conditional. Mutable audit only reads fingerprints, existing certificates, primary metadata and local links.',
})
out.update({
    'current_round_previous_frozen_mathematical_inputs': 403,
    'current_round_new_frozen_mathematical_inputs': len(current_frozen)-323,
    'current_round_new_mathematical_proof_and_review_files': len(proofs)-135,
    'current_round_new_mathematical_producer_runs': 5,
    'current_round_root_own_mathematical_producer_runs': 1,
    'current_round_agents_own_mathematical_producer_runs': 4,
    'current_round_successful_mathematical_producer_runs': 4,
    'current_round_failed_mathematical_producer_runs': 1,
    'current_round_new_mathematical_producer_run_scope': 'Root gcd first1 success, toric capped all-prime LP first1 success, arithmetic actual folded structure first1 success. Quarter original-v1 first1 failed only during huge-Fraction serialization after math assertions; preserved original source with no JSON and never rerun. Distinct v2 first1 success changes serialization only, no old/peer import. Authors total5 runs successful4 failed1. Every independent reviewer reads code and existing certificates only; externalLean0.',
    'current_round_old_or_peer_mathematical_producer_execute_import_rerun': 0,
    'current_round_preserved_failed_source': {
        'file': 'research/cdt_odd_paired_plucker_energy_rate_20261006_verify.py',
        'sha256': current_frozen_pins['cdt_odd_paired_plucker_energy_rate_20261006_verify.py'],
        'execution_count': 1, 'rerun_count': 0, 'json_exists': False,
        'status': 'FAILED serialization, not PASS',
    },
    'current_round_new_source_receipts': 4,
    'current_round_new_source_receipt_pins': [
        {'file': 'literature/' + name, 'sha256': manifest_pins[name], 'file_hash_checked': True}
        for name in [
            'manifest_cdt_odd_paired_rate_units_budget_root_20261006.json',
            'manifest_cdt_odd_paired_plucker_energy_rate_20261006.json',
            'manifest_cdt_odd_paired_all_prime_budget_20261006.json',
            'manifest_cdt_odd_paired_auxiliary_units_structure_20261006.json',
        ]
    ],
    'current_round_new_primary_pdf_files': 3,
    'current_round_new_primary_pdf_pages': 43,
    'current_round_new_primary_html_files': 3,
    'current_round_root_actual_primary_pdf_pages_read': 8,
    'current_round_primary_pdf_reading_scope': 'Root actual Rimanyi-Varchenko PDF1-8 eightpages; Dominici/Rosengren metadata/abstract only, no new Lai reading. Arithmetic author actual8/8/10=26 plus budget-review Lai8-12 five. Toric independent structure actual8/8/10=26 plus own budget Lai8-16 nine,35 total. Quarter newPDF pages0, actual three official DLMF webpage items. Different persons not added into root full reading. Archive43 pages is not all-source full independent proof verification.',
    'current_round_newly_registered_existing_primary_pdf_files': 0,
    'current_round_newly_registered_existing_primary_pdf_pages': 0,
    'current_round_newly_registered_existing_primary_pdf': None,
    'current_round_new_primary_repository_source_files': 0,
    'current_round_new_primary_repository_source_bytes': 0,
    'current_round_external_lean_compilation_and_execution': 0,
    'current_round_complete_external_kernel_proof_revalidation': False,
    'mixed_double_pole_paired_head_free_actual_analytic_n2_rate_proved': True,
    'paired_primitive_binomial_gcd_all_scale_limit_proved': True,
    'paired_primitive_binomial_gcd_B6_gamma_window': ['1.455845','1.457795'],
    'paired_same_basis_all_n_Cauchy_Hardy_analytic_bound_proved': True,
    'paired_same_basis_analytic_beta_H_strict_lower': '8.59403839512558',
    'paired_same_basis_analytic_beta_with_gcd_strict_lower': '11.50572839512558',
    'paired_whole_polynomial_all_prime_signed_common_content_bound_proved': True,
    'paired_all_prime_safe_A_exact': '1085983123/24190320',
    'paired_all_prime_safe_A_window': ['44.893','44.894'],
    'paired_actual_Plucker_weighted_wedge_denominator_interface_proved': True,
    'paired_integer_valued_local_psi_GL_basis_proved': True,
    'paired_local_psi_full_rank_Smith_improvement_proved': False,
    'paired_auxiliary_middle_CRT_Fermat_factorization_proved': True,
    'paired_auxiliary_actual_determinant_Pade_remainder_equivalence_proved': True,
    'paired_auxiliary_middle_rank': 'r, n4r,p18r+1',
    'paired_auxiliary_actual_minimum_pointwise_Pearson_class': '7 for r>=2; full class5, specified polynomial pair scope only',
    'paired_auxiliary_finite_unit_probe_scope': '40 primes p18r+1 with1<=r<=90, p19..1621; maxjointdimension360. Finite only, no infinite unit assertion.',
    'mixed_double_pole_paired_head_free_auxiliary_prime_infinite_two_unit_condition_proved': False,
    'mixed_double_pole_paired_head_free_infinite_nonzero_proved': False,
    'mixed_double_pole_paired_head_free_complete_cheap_gauss_n2_budget_proved': False,
    'mixed_double_pole_matched_strict_positive_margin_proved': False,
    'last_goal_turn_mathematical_progress': 'Actual paired primitive gcd has an all-scale PNT carry integral with B6 gamma1.455845-1.457795 and finite digamma expression. Same actual saturated rank2n Cauchy-Hardy split pays full factorial/basis/symmetric-degree energy; Hardy negative term and exact high real square identity yield betaH>8.59403839512558, same gcd combination>11.50572839512558. Whole-form all-prime signed content model improves coarse60 to exact safeA1085983123/24190320<44.894; actual Plucker wedge and genuine local psi integer-valued GL interfaces proved but full rank/Smith savings unpaid. True auxiliary folded matrices preserve halfjet/middle and PS=u^(9r+1)-u, CRT numerator inverse, exact scalar/matrix Pade remainder gates, middle rankr, full class5/actualclass7 Pearson.40finite primes units do not prove infinite normality/nonzero. Current beta/A bounds do not give strict margin, not an actual-cost no-go. No new special-value or Lean theorem.',
    'current_round_scope': 'Four NEW mathematical papers, four independent root/cross review files, four successful standalone source/certificate sets and one preserved failed-v1 source;17 new mathematical pins, all403 prior unchanged. Four final source receipts, three primaryPDF43 archivepages, three officialHTML snapshots; actual reading by person disclosed. Authors own mathruns5(success4failed1), old/peer execute/import/rerun0, externalLean0. Final draft-status labels in mathematically frozen prose are externally superseded by final receipts; root budget full earlier-text plus final added-paragraph reads accurately distinguished from another all-final-byte reread. Root late final receipts/cross reviews separately logged. Mutable audit checks hashes, existing certificates, metadata and links only.',
})
out.update({'current_round_previous_frozen_mathematical_inputs': 420, 'current_round_new_frozen_mathematical_inputs': 19, 'current_round_new_mathematical_proof_and_review_files': 8, 'current_round_new_mathematical_producer_runs': 6, 'current_round_root_own_mathematical_producer_runs': 3, 'current_round_agents_own_mathematical_producer_runs': 3, 'current_round_successful_mathematical_producer_runs': 5, 'current_round_failed_mathematical_producer_runs': 1, 'current_round_new_mathematical_producer_run_scope': 'Root NEW probe first1PASS105finitecases, NEW carry-v1 first1FAILED guessed decimal interval after exact assertions, preserved source/noJSON/never rerun; distinct NEW-v2 first1PASS42formula comparisons+exact tents. Quarter NEW whole-interval certificate first1PASS4096closedcells; toric NEW jet first1PASS43cases15383checks; arithmetic NEW module first1PASSfivepreviousr14scalar42matrixprofiles. Mathematical proof is paper, probes do not prove infinite units/nonzero. Reviewers all old/peer execute/import/rerun0. Metadata audit only hashes/reads saved files.', 'current_round_old_or_peer_mathematical_producer_execute_import_rerun': 0, 'current_round_preserved_failed_source': {'file': 'research/cdt_odd_paired_dual_plucker_carry_rate_20261006_verify.py', 'sha256': 'ade489f98225ce61a9f58333464ce4d5e91ebfffe149358eb0e4df4b9321c3d5', 'execution_count': 1, 'rerun_count': 0, 'json_exists': False, 'status': 'FAILED wrong guessed decimal window, not PASS'}, 'current_round_new_source_receipts': 4, 'current_round_new_source_receipt_pins': [{'file': 'literature/manifest_cdt_odd_paired_dual_carry_jet_mirror_root_20261006.json', 'sha256': '148d09dce421ceb560bfd0080916826954980586f647f764af35b943a29c6e17', 'file_hash_checked': True}, {'file': 'literature/manifest_cdt_odd_paired_mirror_choice_energy_20261006.json', 'sha256': '8fd3078e221220d293191e716673e45c582b7592ae9f76a4bfcd100263b796fc', 'file_hash_checked': True}, {'file': 'literature/manifest_cdt_odd_paired_large_prime_jet_rank_20261006.json', 'sha256': '9683b3c80fcc2cc512d31d7ba144b27936d8fcf4885ff4222f38369393fec746', 'file_hash_checked': True}, {'file': 'literature/manifest_cdt_odd_paired_auxiliary_pade_symplectic_defect_20261006.json', 'sha256': 'f0502fc3539c08c95aa979c502eb5bda26d8c467734eb406e58ac68304d417da', 'file_hash_checked': True}], 'current_round_new_primary_pdf_files': 3, 'current_round_new_primary_pdf_pages': 76, 'current_round_new_primary_html_files': 0, 'current_round_root_actual_primary_pdf_pages_read': 9, 'current_round_distinct_new_primary_pdf_pages_read_by_team': 32, 'current_round_primary_pdf_reading_scope': 'Root and quarter each actually read Bhargava PDF1-4,7-11 ninepages of31archivepages. Arithmetic author and toric independent reviewer each actually read Beckermann-Labahn1-15 and DAndrea-Krick-Szanto1-8,23pages of45archivepages. Team distinct source pages32, not root full reading or full76page proof revalidation. Root saved/actually read own final receipt before late final arithmetic/toric receipt reads and crossreview; main report records the late complete reads without rewriting frozen root receipt. No certificate bypass.', 'current_round_newly_registered_existing_primary_pdf_files': 0, 'current_round_newly_registered_existing_primary_pdf_pages': 0, 'current_round_newly_registered_existing_primary_pdf': None, 'current_round_new_primary_repository_source_files': 0, 'current_round_new_primary_repository_source_bytes': 0, 'current_round_external_lean_compilation_and_execution': 0, 'current_round_complete_external_kernel_proof_revalidation': False, 'paired_actual_all_prime_weighted_Plucker_duality_proved': True, 'paired_weighted_constraint_all_Smith_layers_zero_one_for_p_gt_n_proved': True, 'paired_exact_carry_defect_n_lt_p_le_2n_proved': True, 'paired_carry_paid_safe_A_gain_exact': '1718/15015', 'paired_carry_third_tent_hidden_by_cap': True, 'paired_actual_unit_tail_weak_kernel_rank_3n_lt_p_le_6n_proved': True, 'paired_whole_X_actual_weak_jet_minor_polygon_proved': True, 'paired_jet_paid_safe_A_gain_exact': '2/3', 'paired_two_disjoint_prime_window_safe_A_combination_proved': True, 'paired_previous_baseline_safe_A_exact': '1085983123/24190320', 'paired_all_prime_safe_A_exact': '4624049789/104824720', 'paired_all_prime_safe_A_window': ['44.112', '44.113'], 'paired_same_basis_mirror_choice_energy_bound_all_n_proved': True, 'paired_same_basis_mirror_cstar_window': ['0.840144459', '0.845115370'], 'paired_same_basis_mirror_beta_strict_lower': '9.09188285412558', 'paired_same_basis_analytic_beta_with_gcd_strict_lower': '12.00357285412558', 'paired_positive_mirror_choice_sum_exact_variational_limit_and_unique_maximizer_proved': True, 'paired_actual_auxiliary_critical_graph_symplectic_defect_pairs_proved': True, 'paired_actual_auxiliary_corank_formula': 'G0=d; M5=d1+d2, with shifted degrees(-d,d),(-d2,-d1,d1,d2)', 'paired_actual_auxiliary_scalar_target_PSC_index': '4r+1', 'paired_actual_nonperfect_intermediate_profile_counterexample': 'r2,p37 firstHankel0, actualsize2det4', 'paired_higher_constraint_Smith_layers_for_p_le_n_proved': False, 'paired_jet_full_Smith_equalities_proved': False, 'paired_actual_cost_lower_bound_or_method_no_go_proved': False, 'mixed_double_pole_paired_head_free_auxiliary_prime_infinite_two_unit_condition_proved': False, 'mixed_double_pole_paired_head_free_infinite_nonzero_proved': False, 'mixed_double_pole_paired_head_free_complete_cheap_gauss_n2_budget_proved': False, 'mixed_double_pole_matched_strict_positive_margin_proved': False, 'new_numerical_irrationality_theorem': False, 'new_lean_formalization': False, 'last_goal_turn_mathematical_progress': 'Same actual paired saturated lattice: exact weighted dual Plucker for all primes and full0/1 Smith whenp>n, exact carry defects n<p<=2n produce genuinely paid1718/15015; exact unit-tail weak ranks3n<p<=6n and whole-X p2 jet polygon produce2/3. Disjoint same-object gains give safeA4624049789/104824720<44.113. Mirror matched coefficient/Hardy penalties rigorously improve same-object analytic rate>12.003572854, with positive choice-sum variational limit and unique maximizer. True middle-corrected auxiliary graph modules have symplectic paired defects and exactcorank G0=d,M5=d1+d2, scalarPSCindex4r+1; actualp37 nonperfect intermediate counterexample rules out circularperfectness. Infinite criticalnormality/nonzero and strictmargin remain open. No new numerical theorem or Lean.', 'current_round_scope': 'Four NEW papers and four NEW independent/root review files;19newmathpins all420previouspreserved. Five new saved-certificate reportsets plus one preservedfailedsource. Own first-only mathruns6(success5failed1), old/peer0, Lean0. Four final source receipts;3default-TLSprimaryPDF76archivepages, no newHTML/repos. Actual reads perperson/source/code/JSON accurately scoped. Root final receipt read before late final arithmetic/toric source receipts and V1-V6 review; main report logs actual late full reads. Mutable audit only checks hashes, saved certificates, metadata and local links.'})
# Latest completed research round; history above remains preserved.
out.update({'current_round_previous_frozen_mathematical_inputs': 439, 'current_round_new_frozen_mathematical_inputs': 16, 'current_round_new_mathematical_proof_and_review_files': 8, 'current_round_new_mathematical_producer_runs': 4, 'current_round_root_own_mathematical_producer_runs': 1, 'current_round_new_mathematical_successful_runs': 4, 'current_round_new_mathematical_failed_runs': 0, 'current_round_first_only_execution_scope': 'Root CRT, quartercap, toricsecondSmith and arithmeticJacobi each own NEW producer firstonce PASS. Old and peer producers execute/import/rerun0; metadata auditor only reads hashes and saved certificates. No auxiliary prime-table extension.', 'current_round_old_or_peer_mathematical_producer_execute_import_rerun': 0, 'current_round_preserved_failed_source': None, 'current_round_new_source_receipts': 4, 'current_round_new_source_receipt_pins': [{'file': 'literature/manifest_cdt_odd_paired_residue_crt_layers_root_20261006.json', 'sha256': 'd315edb66f9c7b3eb7423563a0010772c772a2b5519afc6ebfce6c609f158427', 'file_hash_checked': True}, {'file': 'literature/manifest_cdt_odd_paired_second_smith_layer_20261006.json', 'sha256': '556c65c263154a25e24d93c859a2750460a01eef6d65f8ab1e9e0a94d2678f3e', 'file_hash_checked': True}, {'file': 'literature/manifest_cdt_odd_paired_smith_credit_cap_transfer_20261006.json', 'sha256': 'f8c73f780da60d04a30f484189b9d4004b3ddf5f543b988857d8cffd1d5b3542', 'file_hash_checked': True}, {'file': 'literature/manifest_cdt_odd_paired_auxiliary_boundary_jacobi_krylov_20261006.json', 'sha256': '129070562e4df36e5e0fcfb2b93202bf9d4b015d287fb04ced89bac556a2e1b3', 'file_hash_checked': True}], 'current_round_new_primary_pdf_files': 3, 'current_round_new_primary_pdf_pages': 50, 'current_round_new_primary_html_files': 0, 'current_round_root_actual_primary_pdf_pages_read': 13, 'current_round_distinct_new_primary_pdf_pages_read_by_team': 33, 'current_round_primary_pdf_reading_scope': 'Root actually read Miller1-4/15-16(6), Costas1-4(4), Duran1-3(3):13only. Arithmetic Costas1-18/Duran1-9:27; toricCostas1-5/Duran1-4/8-9:11; quarterMiller6. Union33of50archivepages, not rootfull50reading. Root finald315receipt actually read after all finalpeer mathematical reviews and all finalpeer source receipts. No TLS bypass.', 'current_round_newly_registered_existing_primary_pdf_files': 0, 'current_round_newly_registered_existing_primary_pdf_pages': 0, 'current_round_newly_registered_existing_primary_pdf': None, 'current_round_new_primary_repository_source_files': 0, 'current_round_new_primary_repository_source_bytes': 0, 'current_round_external_lean_compilation_and_execution': 0, 'current_round_complete_external_kernel_proof_revalidation': False, 'paired_actual_all_prime_integral_residue_CRT_GL_proved': True, 'paired_actual_all_prime_ragged_step_Newton_weights': 'p^j*j!, degree<Lr, no local index', 'paired_actual_all_prime_mirror_block_direct_sum_and_Smith_recursion_proved': True, 'paired_actual_all_prime_cheapest_column_baseline_equals_first_n_factorial_proved': True, 'paired_actual_mixed_carry_column_capacity_lower_proved': True, 'paired_actual_mixed_carry_column_capacity_scope': 'p2>8n; delta>=delta0+sum_mixed floor(L/2), actual primitive blocks', 'paired_exact_second_Smith_layer_for_half_window_proved': True, 'paired_exact_second_Smith_layer_scope': 'p>17,n/2<p<=n,p2>8n:0^(p-M),1^(n-p+M-M4),2^M4', 'paired_half_window_first_layer_paid_gain_exact': '121537/4476780', 'paired_M4_and_subhalf_capacity_extra_paid_gain_zero_in_specified_bound_model': True, 'paired_previous_baseline_safe_A_exact': '4624049789/104824720', 'paired_all_prime_safe_A_exact': '790225879771/17925027120', 'paired_all_prime_safe_A_window': ['44.085', '44.086'], 'paired_higher_constraint_Smith_layers_for_p_le_n_proved': False, 'paired_higher_constraint_Smith_layers_scope': 'Exact half-window above; all-prime integral mechanism and capacity lower. No allwindow closed Smith for p<=n/2.', 'paired_actual_middle_preserving_common_selfadjoint_difference_operator_proved': True, 'paired_actual_critical_4seed_8seed_Krylov_units_proved': True, 'paired_actual_Krylov_scope': 'p=18r+1 prime, scalarT<r,matrixQ<3r; auxiliary-local GL only, no global/arch freebasis', 'paired_actual_Jacobi_continuant_and_8seed_moment_recurrence_proved': True, 'paired_actual_8seed_moment_recurrence_order': '5r+1, grows with r', 'paired_actual_endpoint_Weyl_all_prefix_Hankel_units_proved': True, 'paired_actual_dense_seed_outer_connection_degree': '4r', 'mixed_double_pole_paired_head_free_auxiliary_prime_infinite_two_unit_condition_proved': False, 'mixed_double_pole_paired_head_free_infinite_nonzero_proved': False, 'mixed_double_pole_paired_head_free_complete_cheap_gauss_n2_budget_proved': False, 'mixed_double_pole_matched_strict_positive_margin_proved': False, 'paired_actual_cost_lower_bound_or_method_no_go_proved': False, 'new_numerical_irrationality_theorem': False, 'new_lean_formalization': False, 'goal_status': 'active', 'last_goal_turn_mathematical_progress': 'Same actual paired lattice: allprime integral CRT retains complete/ragged degree cutoff and p^j j! costs, actual mirror directsum and finite Schur recursion, exact0/1/2 Smith for p>17,n/2<p<=n,p2>8n. WholeX firstlayercarry credit genuinely pays121537/4476780, giving safeA790225879771/17925027120<44.086; M4/generalcapacity belowhalf hidden by currentcap. Actual chi/halfjet boundaryselfadjoint operator and commonpotential give unitcritical4/8seedKrylov bases, genuineJacobicontinuants/resolvent/momentrecurrence and endpointallprefixunitproducts. Actualouterseedconnections degree4r prevent automatic endpointnormality transfer. Infinite originaltargetunits/nonzero and strictmargin remain open; no new numerical theorem or Lean.', 'current_round_scope': 'Four NEW mathematics and four NEW root/cross reviews;16newmathpins with all439previous unchanged. Four first-only ownproducer/certificate pairs allPASS, failures0, oldpeer0, Lean0. Four finalsource receipts actuallyfullread;3defaultverifiedTLS primaryPDF50archivepages, distinctteamactualpages33/root13, no newHTML/repos. Currentaudit hashes/readssavedcertificates only.', 'current_round_next_mathematical_interfaces': ['Actualsupport-dependent Lambda_IJ correlated with paired CRT packet fees', 'Jacobi resolvent/dense highdegree connections for actualunequal4/8seedmodified minor normality']})
# Latest support/direct-Gram/weighted/modified-target round; all earlier history remains.
out.update({'current_round_previous_frozen_mathematical_inputs': 455, 'current_round_new_frozen_mathematical_inputs': 16, 'current_round_total_frozen_mathematical_inputs': 471, 'current_round_new_mathematical_proof_and_review_files': 8, 'current_round_new_mathematical_producer_runs': 4, 'current_round_root_own_mathematical_producer_runs': 1, 'current_round_agents_own_mathematical_producer_runs': 3, 'current_round_successful_mathematical_producer_runs': 4, 'current_round_failed_mathematical_producer_runs': 0, 'current_round_new_mathematical_successful_runs': 4, 'current_round_new_mathematical_failed_runs': 0, 'current_round_old_or_peer_mathematical_producer_execute_import_rerun': 0, 'current_round_preserved_failed_source': None, 'current_round_first_only_execution_scope': 'Root weighted, quarter support, toric directGram and arithmetic modifiedtarget each own NEW mathematical producer FIRST1PASS, successful source/JSON preserved. No reruns, old/peer execute/import0, no auxiliary-prime table extension. Metadata auditor only hashes and reads saved JSON/files.', 'current_round_new_mathematical_producer_run_scope': 'Four distinct NEW sources each first1PASS: quarter471closed affine pieces/4715checks; toric45actual lift/originalscaledGrammodp2 finitecases+13affine records; root3specified actual jet minors/1425countchecks; arithmetic oldr1,2,4/692structuralchecks. None supplies infinite target normality.', 'current_round_new_source_receipts': 4, 'current_round_new_source_receipt_pins': [{'file': 'literature/manifest_cdt_odd_paired_weighted_support_modified_target_root_20261006.json', 'sha256': '3a29ea816741a59bc70a45878c3edb7cde889e9551eb530cea2caefd5ce2e364', 'file_hash_checked': True}, {'file': 'literature/manifest_cdt_odd_paired_support_correlated_budget_20261006.json', 'sha256': '09d18115750b9488813a6c328c08373d8d939eefb92c199aa458727a0a4d54b9', 'file_hash_checked': True}, {'file': 'literature/manifest_cdt_odd_paired_actual_local_gram_layers_20261006.json', 'sha256': '4086d265702b4a4798eef796579758aeb3c62e997d0b4c51bc934cbd0235f5ce', 'file_hash_checked': True}, {'file': 'literature/manifest_cdt_odd_paired_jacobi_modified_target_normality_20261006.json', 'sha256': 'fa77214875c2beb909739791013054c8dbff87cbf9c587768e1ad2be8295fd4d', 'file_hash_checked': True}], 'current_round_new_primary_pdf_files': 3, 'current_round_new_primary_pdf_pages': 94, 'current_round_new_primary_html_files': 0, 'current_round_root_actual_primary_pdf_pages_read': 19, 'current_round_distinct_new_primary_pdf_pages_read_by_team': 39, 'current_round_primary_pdf_reading_scope': 'Root Grinberg1-4,10-14,31-33=12; Kratt1-3=3; Alvarez8-9,15-16=4:19. Arithmetic Kratt1-5,7-17=16 andAlvarez1-5,8-10,14-16=11:27. Toric Kratt1-3,13-14=5 andAlvarez8-9,15-16=4:9. Quarter0. Source/page union39of94, not sum of persons or full archive reading. Root final receipt actual full reread after all final reviews/peer source receipts; exact source title confirmed againstPDF1 before receipt freeze. Normal verified TLS.', 'current_round_newly_registered_existing_primary_pdf_files': 0, 'current_round_newly_registered_existing_primary_pdf_pages': 0, 'current_round_newly_registered_existing_primary_pdf': None, 'current_round_new_primary_repository_source_files': 0, 'current_round_new_primary_repository_source_bytes': 0, 'current_round_external_lean_compilation_and_execution': 0, 'current_round_complete_external_kernel_proof_revalidation': False, 'paired_actual_integer_valued_ragged_unit_tail_image_cap_proved': True, 'paired_actual_exact_S_coordinate_weak_lifts_proved': True, 'paired_actual_whole_X_direct_Gram_DND_proved': True, 'paired_actual_weak_kernel_scope': 'p>5,p2>8n; ambient degree3n=Qp+R unit sector imageQu+min(R,u), restricted actual rank2n paired weak kernel at least[2n-Qu-min(R,u)]+; no exact paired rank claim.', 'paired_support_p_le_n_paid_gain_exact': '20948066064530861/14991578506784880', 'paired_direct_Gram_n_lt_p_le_2n_paid_gain_exact': '16469/23100', 'paired_actual_joint_node_support_weighted_Omega_bound_proved': True, 'paired_actual_weighted_extra_paid_gain_exact': '1/84', 'paired_actual_weighted_paid_window': '31n/42<p<3n/4 only; relative to current same-window DND max, not raw overlapping gain.', 'paired_previous_baseline_safe_A_exact': '790225879771/17925027120', 'paired_all_prime_safe_A_exact': '45711182732576087/1070827036198920 - 16469/23100 - 1/84', 'paired_all_prime_safe_A_exact_expression': '45711182732576087/1070827036198920 - 16469/23100 - 1/84', 'paired_all_prime_safe_A_approx': '41.963', 'paired_all_prime_safe_A_window': ['41.96', '41.97'], 'paired_all_prime_safe_A_is_upper_bound_not_actual_content': True, 'paired_actual_full_Q_N_profile_unit_proved': True, 'paired_actual_full_Q_block_Hankel_rank': 'N=5r+1, auxiliaryp=18r+1', 'paired_actual_Q_source_minimal_realization': 'N=5r+1', 'paired_actual_fixed_middle_Loewner_and_bordered_target_gates_proved': True, 'paired_actual_finite_support_Christoffel_norm_free_identity_proved': True, 'paired_actual_diagnostic_family_counterexamples': 'p19r1: scalar lambda8, matrixlambda6 singular while ambient/J/raising/fullQ visible. Original fixedlambda2 remainsG1/M15; not originaltarget counterexamples.', 'mixed_double_pole_paired_head_free_auxiliary_prime_infinite_two_unit_condition_proved': False, 'mixed_double_pole_paired_head_free_infinite_nonzero_proved': False, 'mixed_double_pole_paired_head_free_complete_cheap_gauss_n2_budget_proved': False, 'mixed_double_pole_matched_strict_positive_margin_proved': False, 'paired_actual_cost_lower_bound_or_method_no_go_proved': False, 'new_numerical_irrationality_theorem': False, 'new_lean_formalization': False, 'goal_status': 'active', 'last_goal_turn_mathematical_progress': 'Same actual paired degree<3n rank2n lattice: genuine psi GL/ragged unit-tail cap, exact S-coordinate weak lifts and wholeX DND; paid disjoint DeltaC~1.397 andDeltaG16469/23100 plus joint weighted support relative extra1/84 give safeA~41.963 from44.085. FullactualfourQ N-profile and source realization are units/rankN; normfree fixedlambda2 Loewner/bordered/compound gates and finite-support Christoffel proved. Actual diagnosticlambda6/8 counterexamples prevent automatic full-to-critical transfer, not actuallambda2 failures. Infinite originalcritical units/nonzero and strict sameobjectmargin remainopen; no new specialvalue theorem or Lean.', 'current_round_scope': 'Four NEW mathematics and four NEW root/crossreviews,16newmathpins all455previous unchanged; total471. Four own firstonly producers allPASS, failed0, oldpeer0, Lean0. Four final source receipts actually fullread/rootfinalafterallpeers. Three verifiedTLSprimaryPDF94archivepages, teamdistinctactual39/root19; no newHTML/repos. Auditor hashes/savedJSON/metadata/links only.', 'current_round_next_mathematical_interfaces': ['Actual paired image rank and derivative directions in joint weighted support/higherp-layer fees', 'Actual S/K/Z Fermat arithmetic excluding fixed-2 eigenvalue or fixedlambda2 compound cancellation']})
# Latest actual-rank/whole-flow/single-gate/three-seed round; history is preserved.
out.update({
  "current_round_previous_frozen_mathematical_inputs": 471,
  "current_round_new_frozen_mathematical_inputs": 16,
  "current_round_total_frozen_mathematical_inputs": 487,
  "current_round_new_mathematical_proof_and_review_files": 8,
  "current_round_new_mathematical_producer_runs": 4,
  "current_round_root_own_mathematical_producer_runs": 1,
  "current_round_agents_own_mathematical_producer_runs": 3,
  "current_round_successful_mathematical_producer_runs": 4,
  "current_round_failed_mathematical_producer_runs": 0,
  "current_round_new_mathematical_successful_runs": 4,
  "current_round_new_mathematical_failed_runs": 0,
  "current_round_old_or_peer_mathematical_producer_execute_import_rerun": 0,
  "current_round_preserved_failed_source": None,
  "current_round_first_only_execution_scope": "Root singlebordered, quarter actualrank, toric wholeaffine and arithmetic Gosper each distinct own NEW FIRST1PASS; successful sources/results never rerun or modified. No old/peer math execution/import. Quarter actualrank143finitecases is distinct mechanism, not auxiliaryunit table extension. Pure metadata auditor only hashes and reads saved JSON.",
  "current_round_new_mathematical_producer_run_scope": "Root142checks with oldactualr1,2,4 and genericdepthtoy; quarter143cases/124959checks (91exact-domain,52cap-only); toric1601closed affinecells/113merged/266036checks; arithmetic75criticalmomentidentities on oldr1,2,4. Written allscale proofs remain essential; no infinite target normality asserted.",
  "current_round_new_source_receipts": 5,
  "current_round_new_source_receipts_scope": "Root, quarter, toric, arithmetic original frozen final plus distinct final-review-pin supplement. The supplement supersedes original futureV8 plan without rewriting frozen originalreceipt. Root finald5de saved/actually fullread and24physicalpins checked after all finalreviews and fourpeer finalreceipts. No future or reverse pins.",
  "current_round_new_primary_pdf_files": 4,
  "current_round_new_primary_pdf_pages": 125,
  "current_round_new_primary_html_files": 0,
  "current_round_root_actual_primary_pdf_pages_read": 18,
  "current_round_distinct_new_primary_pdf_pages_read_by_team": 24,
  "current_round_primary_pdf_reading_scope": "Root Caruso49-53=5, ElsheikhGiesbrecht1-5=5, Gosper1-3=3, AS1/14-17=5:18 completepages. Arithmetic Gosper1-3 plusAS1-7/14-17=14, toricGosper1-3 plusAS1-3/14-17=10, quarter0. Source/page union24of125archivepages; not perperson sum or full125reading. Root finalaccuratetitles verified againstcover text, partialCaruso covertitle check is not an extra completepage. No TLS bypass.",
  "current_round_newly_registered_existing_primary_pdf_files": 0,
  "current_round_newly_registered_existing_primary_pdf_pages": 0,
  "current_round_newly_registered_existing_primary_pdf": None,
  "current_round_new_primary_repository_source_files": 0,
  "current_round_new_primary_repository_source_bytes": 0,
  "current_round_external_lean_compilation_and_execution": 0,
  "current_round_complete_external_kernel_proof_revalidation": False,
  "paired_actual_unit_sector_supported_primitive_constraint_rank_proved": True,
  "paired_actual_unit_sector_constraint_rank": "f=a*u-a*(2u-V)_+/2=a*min(u,V/2), highcarryunithead forcedzero",
  "paired_actual_unit_sector_exact_image_rank_proved": True,
  "paired_actual_unit_sector_exact_image_rank_scope": "p>5,p<=2n,p2>8n,Q>=a+1: rankQu+min(R,u)-f. Q=a only upperrank cap. Actual primitive split, real raggedtop and originalS char0lift.",
  "paired_actual_weak_kernel_scope": "p>5,p<=2n,p2>8n actualpaired kernel >=[2n-Qu-min(R,u)+f]+; exactQ>=a+1. Whole-X DND sameS. Arbitrary partialweightedrow f-transfer stillunproved.",
  "paired_actual_unit_sector_independent_paid_gain_exact": "19/980",
  "paired_actual_integer_weighted_Omega_exact_coupon_flow_proved": True,
  "paired_actual_integer_weighted_Omega_dual_candidate_count": 36,
  "paired_actual_integer_weighted_Omega_dual_vertices": "lambda0..11,eta0,1,2; integralcapacitatedflow/prefixexchange/attainedpolyhedraldual",
  "paired_weighted_Omega_only_current_paid_gain_exact": "1433895329207009209/2765986534444032900",
  "paired_weighted_Omega_only_safe_A_exact": "90135864061549507/2174857836049080",
  "paired_actual_rank_weighted_common_max_paid_gain_exact": "4594551260881450309261834591/2837232739731183068973297600",
  "paired_actual_rank_weighted_common_max_covers": "[1/4,6],1601closedaffinecells/113merged; commonmax471/Omega/actualpair, neitherOmegaonly nor19/980 separatelyadded",
  "paired_previous_baseline_safe_A_exact": "224674976889262531/5354135180994600",
  "paired_all_prime_safe_A_exact": "68678357676574195925297901887/1702339643838709841383978560",
  "paired_all_prime_safe_A_exact_expression": "68678357676574195925297901887/1702339643838709841383978560",
  "paired_all_prime_safe_A_approx": "40.343510723692695",
  "paired_all_prime_safe_A_window": [
    "40.343",
    "40.344"
  ],
  "paired_all_prime_safe_A_is_upper_bound_not_actual_content": True,
  "paired_all_prime_safe_A_normalization_scope": "Signed rational Q_n with D_A/Q_n integral and log|Q_n^-1| fee; positivecontent retained. Not raw minimalintegerdenominator upper or actualcostlower.",
  "paired_actual_single_M5_leading_gate_without_G0_unit_proved": True,
  "paired_actual_single_M5_leading_gate_scope": "Actualp18r+1,m2r: p17mD_A whole-X reduction knownunit*detM5 and corankNcal=corankM5, nounknownGinverses",
  "paired_actual_original_leading_gate_requires_two_units": False,
  "paired_actual_degenerate_strong_Gram_Smith_under_M5_unit_proved": True,
  "paired_actual_degenerate_strong_Gram_Smith": "0^(5m/2-g),1^(2g),2^(3m/2-g), g=corankG0; M5unitcondition",
  "paired_whole_X_depth2_conditional_perturbation_gate_proved": True,
  "paired_whole_X_depth2_conditional_perturbation_gate_scope": "ActualN_X in p3; if N(c)invertible,maxSmith<=2 thenwholeXnormalizeddet unit. Genericdepth3 exactcounterexample sharp; actualhigherlayerconditionunproved.",
  "paired_actual_higher_layer_max_Smith_le_2_proved": False,
  "paired_actual_fixed_lambda2_Gosper_critical_operators_and_boundary_proved": True,
  "paired_actual_fixed_lambda2_constant_number_seed_reduction_proved": True,
  "paired_actual_fixed_lambda2_unknown_seed_count": 3,
  "paired_actual_fixed_lambda2_unknown_seed_scope": "ActualA0=G1,A1=G(y2),B0=H1; crossallmoments explicitboundaries, truefirstpole/middlemask retained, fixed13/18,5/18.",
  "paired_actual_fixed_lambda2_M5_three_seed_polynomial_identity_proved": True,
  "paired_actual_fixed_lambda2_full_cubic_Dixon_unit_proved": True,
  "paired_actual_fixed_lambda2_incomplete_middle_unit_proved": False,
  "paired_actual_fixed_lambda2_Hasse_fixed_family_identified": False,
  "mixed_double_pole_paired_head_free_auxiliary_prime_infinite_two_unit_condition_proved": False,
  "mixed_double_pole_paired_head_free_auxiliary_prime_infinite_single_M5_unit_condition_proved": False,
  "mixed_double_pole_paired_head_free_infinite_nonzero_proved": False,
  "mixed_double_pole_paired_head_free_complete_cheap_gauss_n2_budget_proved": False,
  "mixed_double_pole_matched_strict_positive_margin_proved": False,
  "paired_actual_cost_lower_bound_or_method_no_go_proved": False,
  "new_numerical_irrationality_theorem": False,
  "new_lean_formalization": False,
  "goal_status": "active",
  "last_goal_turn_mathematical_progress": "Actualpaired saturatedS: supportedprimitive constraints and exactunitsector rank whenQ>=a+1 retain raggedtop/outsidehead lifts. JointweightedOmega exactly36dualvertices, complete commonmax withactualrank genuinelypays1.619377640946, sameS signedscale safeA40.343510723692. Actual normalized wholeX criticalleading gate needsM5 alone, permits singularG0, gives conditional0/1/2Smith and sharp p3/depth2 higherlayer alternative. Fixedoriginallambda2 allcriticalG/C/Hmoments reduce by three nonresonant Gosperoperators/trueboundaries to actualA0,A1,B0; crossfullyexplicit,fullcubicDixonunit butincompletemiddlekept. InfiniteactualM5/nonzero andstrictmargin remainopen; nonewnumericaltheorem/Lean.",
  "current_round_scope": "FourNEW principalmaths andfourNEW formalroot/crossreviews;16newmathpins all471previous preserved,total487. Fourown FIRST1 allPASS,mathfailed0,oldpeer0,Lean0. Fivefinalsource receipts includingone distinct supplement, rootactualfinalreadafterallpeers. FourverifiedTLS primaryPDF125archivepages, teamdistinctactual24/root18. No newHTML/repos. Pureaudit hashes/savedJSON/source/linkmetadata only.",
  "current_round_next_mathematical_interfaces": [
    "Actualfixed three-seed polynomial anti-cancellation allowing singularintermediateprofiles",
    "ActualhigherlayerSmith resolving M5modp singularity via p3 perturbation gate",
    "Primitive constraint rank visible to chosenweighted jetrow support"
  ]
})
out['current_round_new_source_receipt_pins'] = [
    {'file': 'literature/'+name, 'sha256': expected, 'file_hash_checked': True}
    for name, expected in latest_rank_flow_gate_gosper_manifest_pins.items()
]
# Completed supported/Racah/depth4 round; historical output updates remain above.
out.update({'as_of': '2026-10-07', 'current_round_previous_frozen_mathematical_inputs': 487, 'current_round_new_frozen_mathematical_inputs': 16, 'current_round_new_frozen_execution_guard_records': 1, 'current_round_new_frozen_records': 17, 'current_round_total_frozen_mathematical_inputs': 503, 'current_round_total_frozen_records': 504, 'current_round_new_mathematical_proof_and_review_files': 8, 'current_round_new_mathematical_producer_runs': 4, 'current_round_root_own_mathematical_producer_runs': 1, 'current_round_agents_own_mathematical_producer_runs': 3, 'current_round_successful_mathematical_producer_runs': 4, 'current_round_failed_mathematical_producer_runs': 0, 'current_round_new_mathematical_successful_runs': 4, 'current_round_new_mathematical_failed_runs': 0, 'current_round_old_or_peer_mathematical_producer_execute_import_rerun': 0, 'current_round_preserved_failed_source': None, 'current_round_first_only_execution_scope': 'Quarter supported, toric transfer, root valueGram and arithmetic Racah each distinct own NEW producer FIRST1PASS; successful source/results frozen, old/peer execute/import/rerun0, no auxiliary unit-prime-table extension. Pure audit only hashes and parses saved records.', 'current_round_new_mathematical_producer_run_scope': 'Quarter17059checks/6originalS cases/30profiles/12actual partial-support counterexamples; toric12141endpoint-area checks/213internal cells/98saved mergedrecords; root66037mechanism checks on oldr1,2,4 plus depthtoys, no actualanchor higherSmith; arithmetic937moment/border/displacement identities oldr1,2,4, no infiniteunit assertion. Written all-scale proofs remain essential.', 'current_round_new_source_receipts': 4, 'current_round_new_source_receipts_scope': 'Four final receipts. Root646c created after actual final FULL reads of all three final peer receipts and four formalreviews, then complete actual selfread/JSONparse and23physical pins checked. No mutable-main/audit current required pins or future/reverse cycles.', 'current_round_new_source_receipt_pins': [{'file': 'literature/manifest_cdt_odd_paired_selected_jet_primitive_support_20261006.json', 'sha256': '893e384530589795701cf8506650547a118042c5632d18486e910b6d7113eedc', 'file_hash_checked': True}, {'file': 'literature/manifest_cdt_odd_paired_supported_weighted_dual_transfer_20261006.json', 'sha256': 'a286feded461742efb471990c277f22a3c111401d6f321b31c6399e4a0f2f25c', 'file_hash_checked': True}, {'file': 'literature/manifest_cdt_odd_paired_fixed_middle_racah_border_20261006.json', 'sha256': 'a5ac5eb90cfbc43057f69a5f0d21b000af1dd672d0a7299015c085e89a62f1fa', 'file_hash_checked': True}, {'file': 'literature/manifest_cdt_odd_paired_supported_racah_depth4_root_20261006.json', 'sha256': '646c34c4c34fb45092b2c9b4d4f173f7dc225ba063ec02e541638cc9e3853663', 'file_hash_checked': True}], 'current_round_new_primary_pdf_files': 3, 'current_round_new_primary_pdf_pages': 233, 'current_round_new_primary_html_files': 0, 'current_round_root_actual_primary_pdf_pages_read': 9, 'current_round_distinct_new_primary_pdf_pages_read_by_team': 28, 'current_round_primary_pdf_reading_scope': 'Root KS1,28-31,54-57=9; Racah norms28-30,54-57 are limit relations. Arithmetic Pearson1-10,13-15=13; Li-Long-Tu1-5=5; KS7,28-30=4:22. Toric Pearson1-3,8-9=5; LLT1-2=2; KS28-30=3:10, all within arithmetic readscope. Quarter0. Team source/page union28, not sum41 or archive233/fullproof revalidation. Normal verified TLS.', 'current_round_newly_registered_existing_primary_pdf_files': 0, 'current_round_newly_registered_existing_primary_pdf_pages': 0, 'current_round_newly_registered_existing_primary_pdf': None, 'current_round_new_primary_repository_source_files': 0, 'current_round_new_primary_repository_source_bytes': 0, 'current_round_external_lean_compilation_and_execution': 0, 'current_round_complete_external_kernel_proof_revalidation': False, 'paired_actual_weak_kernel_scope': 'Original rank2n saturated paired lattice remains. Supported coefficient-source rank for p>5,p<=2n,p2>8n subtracts f_B on actually visible big-source constraints before observation, with ragged top preserved; arbitrary globalf subtraction is invalid.', 'paired_actual_selected_jet_supported_primitive_rank_proved': True, 'paired_actual_selected_jet_supported_primitive_rank_formula': 'rankY_I <= sum min(r_rho,Q)+min(R,|B|)-f_B, f_B=a|C\\sigma U|+(a/2)|C intersection sigma C|', 'paired_actual_selected_jet_left_right_matched_node_counts_proved': True, 'paired_actual_supported_weighted_dual_transfer_proved': True, 'paired_actual_supported_weighted_dual_candidate_count': 27, 'paired_actual_supported_weighted_dual_transfer_scope': 'lambda3..11,eta0,1,2, missing-support priced gap>=2a pays graph-deleted constraints; legal all-X bound -10n+Phi+2f, not naive adding globalf to oldOmega. T18lambda2 uncounted.', 'paired_actual_supported_weighted_paid_gain_exact': '589881521281691/20345444272717200', 'paired_actual_selected_jet_hand_window_paid_gain_exact': '1/216 already included in common max', 'paired_actual_supported_weighted_common_max_cover': 'Update[1/4,2],113old literal rows/106intersecting update,213internal cells,98saved merged records; old[2,6] bound preserved.', 'paired_actual_supported_weighted_floor_jump_scope': 'Uniform1116 only on open fixedfloor cells. Finite rational cuts at eachn use actual integer formula or old fallback, extra O(nlogn)=o(n2); affineclosed endpoints cover integral extensions only.', 'paired_previous_baseline_safe_A_exact': '68678357676574195925297901887/1702339643838709841383978560', 'paired_all_prime_safe_A_exact': '800671681093752110193539327219/19860629178118281482813083200', 'paired_all_prime_safe_A_exact_expression': '800671681093752110193539327219/19860629178118281482813083200', 'paired_all_prime_safe_A_approx': '40.314517426059346', 'paired_all_prime_safe_A_window': ['40.314', '40.315'], 'paired_all_prime_safe_A_is_upper_bound_not_actual_content': True, 'paired_all_prime_safe_A_normalization_scope': 'Signed rational Q_n with D_A/Q_n integral and log|Q_n^-1| safe upper fee, positivecontent retained; not actual minimum integer denominator or actual-cost lower bound.', 'paired_actual_value_Gram_all_unit_nodes_weak_p_divisibility_proved': True, 'paired_actual_value_Gram_normalized_whole_X_precision': 5, 'paired_actual_value_Gram_precision_scope': 'p>5,p2>8n,p<=6n includingQ0,a0: unit tail h>=Q+1 implies localPhi identically0; all unit head/tail weakvalues p-divisible, nonunitW>=p2, normalized valueGram integral and N_X=24p5H.', 'paired_whole_X_depth4_conditional_perturbation_gate_proved': True, 'paired_whole_X_depth4_conditional_perturbation_gate_scope': 'If actual N(c) is invertible and maxSmith<=4, normalized detN(X)/detN(c) modp constant1. Genericdepth5 boundary toy is not an actual targetcounterexample; infiniteactual terminationunproved.', 'paired_actual_higher_layer_max_Smith_le_4_proved': False, 'paired_actual_higher_residual_Schur_ladder_proved': True, 'paired_actual_higher_residual_Schur_ladder_scope': 'Only identified unitblock inverses, divide residual byp stages0..4; k5=0 iff invertible anchor with maxSmith<=4, terminating detvaluation=sumk1..k4. Finite mechanism does not compute actual anchor higherSmith.', 'paired_actual_fixed_lambda2_complete_cubic_Racah_identification_proved': True, 'paired_actual_fixed_lambda2_complete_cubic_all_Hankel_profiles_unit_proved': True, 'paired_actual_fixed_lambda2_complete_cubic_all_Hankel_profiles_scope': 'p18r+1,a5r, everydegree0<=j<=a norm and leading coefficientunit; retain original halfweight at0 and true middle cutoffs.', 'paired_actual_fixed_lambda2_known_complete_CD_kernel_proved': True, 'paired_actual_fixed_lambda2_actual_middle_rank_update': 'rankr, H_actual=D+VEVt; D/E unit', 'paired_actual_fixed_lambda2_actual_2r_border_gate_proved': True, 'paired_actual_fixed_lambda2_actual_2r_border_gate_scope': 'Only knownunitD/E inverses; detM5=(-1)^r detE detD detN_2r and corankM5=corankN_2r. True4r leading criterion compressed to2r, originalS rank unchanged.', 'paired_actual_fixed_lambda2_unknown_seed_count': 2, 'paired_actual_fixed_lambda2_unknown_seed_scope': 'Only actual fifthpowerA0/A1 retained in r-by-r upper-left structuredborder block; cubicB0 determined by same known full Racahkernel and actual middlemask. This does not prove actualmiddle unit or absence of generalmixedkernel.', 'paired_actual_fixed_lambda2_middle_spectral_displacement_rank': 2, 'paired_actual_fixed_lambda2_nonzero_spectral_invariant_kernel_excluded': True, 'paired_actual_fixed_lambda2_general_mixed_kernel_excluded': False, 'paired_actual_fixed_lambda2_two_sided_Pearson_and_true_boundary_proved': True, 'paired_actual_fixed_lambda2_leading_radical_dimension_bound': '<=2r with corankM5=corankN_2r', 'mixed_double_pole_paired_head_free_auxiliary_prime_infinite_single_M5_unit_condition_proved': False, 'mixed_double_pole_paired_head_free_infinite_nonzero_proved': False, 'mixed_double_pole_matched_strict_positive_margin_proved': False, 'new_numerical_irrationality_theorem': False, 'new_lean_formalization': False, 'goal_status': 'active', 'last_goal_turn_mathematical_progress': 'Supported coefficient-space primitive constraints and matched nodecounts yield full weighted transfer, paid sameS gain0.0289932976 and signed safeA40.314517426059. Actual valueGram precisionp5 yields conditional maxSmith4 wholeX constantnonzero gate and exact higherresidual ladder. Complete cubic halfjet Racah all norms/profiles unit, knownCD and rankr actualmiddle update yield exact actual4r->2r gate/corank, rank2 spectralcommutator and no spectralinvariantkernel. Generalmixedkernel/infinite highertermination/nonzero and strict sameobjectmargin remainopen; no numerical theorem or Lean.', 'current_round_scope': 'FourNEW principalmaths/fourformalreviews,16newmathfiles plus1immutable executionguard, all487previouspreserved; total504records (503mathfiles+1guard). Fourdistinct FIRST1successes failed0 oldpeer0 Lean0, no auxunit-table extension. Four final receipts/root finalafter allpeer finalreads. ThreeverifiedTLSprimaryPDF233archivepages, teamactual28/root9, no newHTML/repos. Pureaudit hashes/savedJSON/provenance/links only.', 'current_round_next_mathematical_interfaces': ['Actual originalfixedlambda2 2r mixed-boundary anti-cancellation.', 'Actual leadingradical higher p-adic residual ranks and termination within4layers.', 'Additional truly supported weighted gains relative current commonmax; lambda2 T18 unpaid.']})
Path(__file__).with_suffix('.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'status': out['status'], 'frozen_files': len(frozen),
                  'current_frozen_inputs': len(current_frozen),
                  'technical_report_sets': len(reports), 'proof_review_files': len(proofs),
                  'source_pdfs': len(pdfs), 'source_pdf_pages': out['original_pdf_pages'],
                  'local_links_checked': links}, ensure_ascii=False))
