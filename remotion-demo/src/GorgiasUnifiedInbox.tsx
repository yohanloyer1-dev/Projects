import { AbsoluteFill, useCurrentFrame, useVideoConfig, interpolate, spring } from "remotion";

// Gorgias brand colors
const COLORS = {
  dark: "#101010",
  coral: "#FF6D62",
  peach: "#FF9780",
  cream: "#FFF9F4",
};

// Channel icons as simple SVG components
const EmailIcon: React.FC<{ color: string; size: number }> = ({ color, size }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth={2}>
    <rect x="2" y="4" width="20" height="16" rx="2" />
    <path d="M22 6L12 13L2 6" />
  </svg>
);

const ChatIcon: React.FC<{ color: string; size: number }> = ({ color, size }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth={2}>
    <path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z" />
  </svg>
);

const PhoneIcon: React.FC<{ color: string; size: number }> = ({ color, size }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth={2}>
    <path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07 19.5 19.5 0 01-6-6 19.79 19.79 0 01-3.07-8.67A2 2 0 014.11 2h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L8.09 9.91a16 16 0 006 6l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z" />
  </svg>
);

const SocialIcon: React.FC<{ color: string; size: number }> = ({ color, size }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth={2}>
    <circle cx="12" cy="12" r="10" />
    <path d="M2 12h20M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10 15.3 15.3 0 014-10z" />
  </svg>
);

const SmsIcon: React.FC<{ color: string; size: number }> = ({ color, size }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth={2}>
    <rect x="5" y="2" width="14" height="20" rx="2" />
    <circle cx="12" cy="18" r="1" fill={color} />
  </svg>
);

const InboxIcon: React.FC<{ color: string; size: number }> = ({ color, size }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth={2.5}>
    <polyline points="22 12 16 12 14 15 10 15 8 12 2 12" />
    <path d="M5.45 5.11L2 12v6a2 2 0 002 2h16a2 2 0 002-2v-6l-3.45-6.89A2 2 0 0016.76 4H7.24a2 2 0 00-1.79 1.11z" />
  </svg>
);

interface ChannelConfig {
  Icon: React.FC<{ color: string; size: number }>;
  startX: number;
  startY: number;
  delay: number;
  label: string;
}

const channels: ChannelConfig[] = [
  { Icon: EmailIcon, startX: -500, startY: -250, delay: 0, label: "Email" },
  { Icon: ChatIcon, startX: 500, startY: -200, delay: 6, label: "Chat" },
  { Icon: PhoneIcon, startX: -450, startY: 250, delay: 12, label: "Voice" },
  { Icon: SocialIcon, startX: 500, startY: 220, delay: 4, label: "Social" },
  { Icon: SmsIcon, startX: 0, startY: -400, delay: 8, label: "SMS" },
];

export const GorgiasUnifiedInbox: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const flyDuration = fps * 1.2;
  const mergeFrame = fps * 2;

  return (
    <AbsoluteFill
      style={{
        backgroundColor: COLORS.dark,
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      {/* Subtle radial gradient background */}
      <div
        style={{
          position: "absolute",
          width: "100%",
          height: "100%",
          background: `radial-gradient(ellipse at center, #1a1a1a 0%, ${COLORS.dark} 70%)`,
        }}
      />

      {/* Flying channel icons */}
      {channels.map(({ Icon, startX, startY, delay, label }, i) => {
        const x = interpolate(
          frame,
          [delay, delay + flyDuration],
          [startX, 0],
          { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
        );

        const y = interpolate(
          frame,
          [delay, delay + flyDuration],
          [startY, 0],
          { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
        );

        const fadeIn = interpolate(
          frame,
          [delay, delay + 10],
          [0, 1],
          { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
        );

        const fadeOut = interpolate(
          frame,
          [mergeFrame, mergeFrame + 15],
          [1, 0],
          { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
        );

        const opacity = Math.min(fadeIn, fadeOut);

        const scale = interpolate(
          frame,
          [delay, delay + flyDuration],
          [0.6, 1],
          { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
        );

        return (
          <div
            key={i}
            style={{
              position: "absolute",
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
              gap: 8,
              transform: `translate(${x}px, ${y}px) scale(${scale})`,
              opacity,
            }}
          >
            <div
              style={{
                width: 80,
                height: 80,
                borderRadius: 16,
                backgroundColor: "rgba(255, 249, 244, 0.1)",
                border: "2px solid rgba(255, 249, 244, 0.2)",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
              }}
            >
              <Icon color={COLORS.cream} size={40} />
            </div>
            <span
              style={{
                color: COLORS.cream,
                fontSize: 16,
                fontWeight: 500,
                fontFamily: "system-ui, -apple-system, sans-serif",
              }}
            >
              {label}
            </span>
          </div>
        );
      })}

      {/* Central glow */}
      <div
        style={{
          position: "absolute",
          width: 300,
          height: 300,
          borderRadius: "50%",
          background: `radial-gradient(circle, ${COLORS.coral}40 0%, transparent 70%)`,
          filter: "blur(40px)",
          opacity: interpolate(
            frame,
            [mergeFrame, mergeFrame + 20],
            [0, 1],
            { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
          ),
        }}
      />

      {/* Central unified inbox icon */}
      {(() => {
        const inboxOpacity = interpolate(
          frame,
          [mergeFrame + 10, mergeFrame + 25],
          [0, 1],
          { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
        );

        const inboxScale = spring({
          frame: frame - mergeFrame - 10,
          fps,
          config: { damping: 10, stiffness: 150 },
        });

        return (
          <div
            style={{
              position: "absolute",
              width: 120,
              height: 120,
              borderRadius: 24,
              backgroundColor: COLORS.coral,
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              opacity: inboxOpacity,
              transform: `scale(${Math.max(0, inboxScale)})`,
              boxShadow: `0 0 80px ${COLORS.coral}80`,
            }}
          >
            <InboxIcon color={COLORS.dark} size={60} />
          </div>
        );
      })()}

      {/* Tagline */}
      {(() => {
        const taglineDelay = mergeFrame + 40;
        const taglineOpacity = interpolate(
          frame,
          [taglineDelay, taglineDelay + 20],
          [0, 1],
          { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
        );
        const taglineY = interpolate(
          frame,
          [taglineDelay, taglineDelay + 20],
          [30, 0],
          { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
        );

        return (
          <div
            style={{
              position: "absolute",
              bottom: 180,
              textAlign: "center",
              opacity: taglineOpacity,
              transform: `translateY(${taglineY}px)`,
            }}
          >
            <p
              style={{
                color: COLORS.cream,
                fontSize: 56,
                fontWeight: 600,
                fontFamily: "system-ui, -apple-system, sans-serif",
                margin: 0,
                marginBottom: 12,
              }}
            >
              One inbox. Every channel.
            </p>
            <p
              style={{
                color: "rgba(255, 249, 244, 0.6)",
                fontSize: 24,
                fontWeight: 400,
                fontFamily: "system-ui, -apple-system, sans-serif",
                margin: 0,
                letterSpacing: 2,
              }}
            >
              Email • Chat • SMS • Social • Voice
            </p>
          </div>
        );
      })()}

      {/* Gorgias logo */}
      {(() => {
        const logoOpacity = interpolate(
          frame,
          [fps * 4, fps * 4.3],
          [0, 1],
          { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
        );

        return (
          <div
            style={{
              position: "absolute",
              bottom: 40,
              right: 50,
              display: "flex",
              alignItems: "center",
              gap: 12,
              opacity: logoOpacity,
            }}
          >
            <div
              style={{
                width: 44,
                height: 44,
                borderRadius: 10,
                backgroundColor: COLORS.coral,
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                fontWeight: 700,
                fontSize: 24,
                color: COLORS.dark,
                fontFamily: "system-ui, -apple-system, sans-serif",
              }}
            >
              G
            </div>
            <span
              style={{
                fontSize: 28,
                fontWeight: 500,
                color: COLORS.cream,
                fontFamily: "system-ui, -apple-system, sans-serif",
              }}
            >
              gorgias
            </span>
          </div>
        );
      })()}
    </AbsoluteFill>
  );
};
