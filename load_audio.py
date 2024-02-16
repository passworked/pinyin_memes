import whisperx
import json
def trans_audio_to_whisper(path='./words_list'):

    device = "cuda"
    batch_size = 16
    language = 'zh'
    compute_type = "float16"

    model = whisperx.load_model(
        "large-v2", device, compute_type=compute_type, language=language)
    audio = whisperx.load_audio(path)
    result = model.transcribe(audio, batch_size=batch_size)
    model_a, metadata = whisperx.load_align_model(
        language_code=language, device=device)
    result = whisperx.align(result["segments"], model_a,
                            metadata, audio, device, return_char_alignments=False)

    return result["word_segments"]


words_list = [{'word': '一', 'start': 0.521, 'end': 0.661, 'score': 0.981}, {'word': '百', 'start': 0.661, 'end': 0.822, 'score': 0.999}, {'word': '年', 'start': 0.822, 'end': 1.042, 'score': 0.997}, {'word': '前', 'start': 1.042, 'end': 1.623, 'score': 0.957}, {'word': '人', 'start': 1.623, 'end': 2.123, 'score': 0.958}, {'word': '類'}, {'word': '發'}, {'word': '明', 'start': 2.123, 'end': 2.484, 'score': 0.879}, {'word': '了', 'start': 2.484, 'end': 2.624, 'score': 0.862}, {'word': '味', 'start': 2.624, 'end': 2.844, 'score': 0.908}, {'word': '精', 'start': 2.844, 'end': 3.305, 'score': 0.954}, {'word': '二', 'start': 3.305, 'end': 3.505, 'score': 0.996}, {'word': '十', 'start': 3.505, 'end': 3.646, 'score': 0.766}, {'word': '年', 'start': 3.646, 'end': 3.866, 'score': 0.974}, {'word': '前', 'start': 3.866, 'end': 4.306, 'score': 0.997}, {'word': '太', 'start': 4.306, 'end': 4.547, 'score': 0.994}, {'word': '太', 'start': 4.547, 'end': 5.328, 'score': 0.949}, {'word': '樂'}, {'word': '創'}, {'word': '造', 'start': 5.328, 'end': 5.488, 'score': 0.993}, {'word': '了', 'start': 5.488, 'end': 5.608, 'score': 0.982}, {'word': '雞'}, {'word': '精', 'start': 5.608, 'end': 5.809, 'score': 0.9}, {'word': '今', 'start': 5.809, 'end': 6.49, 'score': 0.927}, {'word': '天', 'start': 6.49, 'end': 6.93, 'score': 0.955}, {'word': '太', 'start': 6.93, 'end': 7.13, 'score': 0.995}, {'word': '太', 'start': 7.13, 'end': 7.531, 'score': 0.928}, {'word': '樂'}, {'word': '唱', 'start': 7.531, 'end': 7.751, 'score': 0.911}, {'word': '到', 'start': 7.751, 'end': 7.932, 'score': 0.943}, {'word': '仙', 'start': 7.932, 'end': 8.272, 'score': 0.905}, {'word': '上', 'start': 8.272, 'end': 8.512, 'score': 0.995}, {'word': '加', 'start': 8.512, 'end': 8.733, 'score': 0.909}, {'word': '仙', 'start': 8.733, 'end': 9.313, 'score': 0.967}, {'word': '加', 'start': 9.313, 'end': 9.834, 'score': 0.937}, {'word': '一', 'start': 9.834, 'end': 10.034, 'score': 0.9}, {'word': '點'}, {'word': '雞'}, {'word': '精', 'start': 10.034, 'end': 10.495, 'score': 0.948}, {'word': '加', 'start': 10.495, 'end': 10.735, 'score': 0.912}, {'word': '一', 'start': 10.735, 'end': 11.296, 'score': 0.945}, {'word': '點'}, {'word': '蔬'}, {'word': '汁', 'start': 11.296, 'end': 11.396, 'score': 0.799}, {'word': '仙', 'start': 11.396, 'end': 11.937, 'score': 0.939}, {'word': '加', 'start': 11.937, 'end': 12.157, 'score': 0.908}, {'word': '一', 'start': 12.157, 'end': 12.658, 'score': 0.908}, {'word': '點'}, {'word': '雞'}, {'word': '汁', 'start': 12.658, 'end': 13.199, 'score': 0.913}, {'word': '味', 'start': 13.199, 'end': 13.459, 'score': 0.924}, {'word': '道', 'start': 13.459, 'end': 13.86, 'score': 0.949}, {'word': '好', 'start': 13.86, 'end': 14.461, 'score': 0.935}, {'word': '極'}, {'word': '了', 'start': 14.461, 'end': 14.481, 'score': 0.998}]
with open('words_list.json','w',encoding='utf-8') as f:
    json.dump(words_list,f)
