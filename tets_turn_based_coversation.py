# test_turnbasedconversation.py

from vocode.turn_based.synthesizer.gtts_synthesizer import GTTSSynthesizer
from vocode.turn_based.output_device.speaker_output import SpeakerOutput
from vocode.turn_based.input_device.microphone_input import MicrophoneInput
from vocode.turn_based.transcriber.deepgram_transcriber import DeepgramTranscriber
from vocode.turn_based.agent.groq_agent import GroqAgent
import sounddevice as sd
from vocode.turn_based.turn_based_conversation import TurnBasedConversation  # rename if needed
import os

# Load your API keys from env or paste directly here
GROQ_API_KEY = "GROQ_API_KEY"
DEEPGRAM_API_KEY = "DEEPGRAM_API_KEY"

def test_turn_based_conversation():
    print("Initializing test for TurnBasedConversation...")
    # devices = sd.query_devices()
    # print(devices)
    # device_id = int(input("Enter input device index: "))
    # sd.default.device = device_id


    
 
    # input_devices = [d for d in devices if d["max_input_channels"] > 0]

    # Set up each component
    input_device = MicrophoneInput.from_default_device()
    transcriber = DeepgramTranscriber(api_key=DEEPGRAM_API_KEY)
    agent = GroqAgent(
        api_key=GROQ_API_KEY,
        model_name="llama3-8b-8192",
        system_prompt="You're a helpful assistant.",
        initial_message="Hi! I'm ready to chat. Say something!"
    )
    synthesizer = GTTSSynthesizer()
    output_device = SpeakerOutput.from_default_device()

    # Build the conversation
    convo = TurnBasedConversation(
        input_device=input_device,
        transcriber=transcriber,
        agent=agent,
        synthesizer=synthesizer,
        output_device=output_device
    )

    # Start listening and processing one response
    # input("Press Enter to start speaking...")
    # convo.start_speech()
    # input("Press Enter to stop speaking and get a response...")
    # convo.end_speech_and_respond()

    # print("Conversation cycle complete.")
    # output_device.terminate()


    try:
        while True:
            user_input = input("🎙️ Press Enter to speak (or type 'q' to quit): ")
            if user_input.strip().lower() == 'q':
                break

            convo.start_speech()
            input("Press Enter to stop speaking and get a response...")
            convo.end_speech_and_respond()
    except KeyboardInterrupt:
        print("\nConversation interrupted by user.")
    finally:
        print("Ending conversation.")
        output_device.terminate()

if __name__ == "__main__":
    test_turn_based_conversation()
