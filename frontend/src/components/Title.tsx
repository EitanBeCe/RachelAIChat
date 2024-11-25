import { useState } from "react";

type Props = {
  setMessages: any;
};

function Title({ setMessages }: Props) {
	const [isResetting, setIsResetting] = useState(false)

	// Reset the conversation
	const resetConversation = async () => {
		setIsResetting(true)
		setIsResetting(false)
	}

  return <div>Title</div>;
}

export default Title;
