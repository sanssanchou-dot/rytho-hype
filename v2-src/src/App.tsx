import { MotionConfig } from "motion/react"
import { TooltipProvider } from "@/components/ui/tooltip"
import { AppProvider } from "@/app-state"
import { useBreathingLight } from "@/lib/glass"
import { Nav } from "@/sections/Nav"
import { Hero } from "@/sections/Hero"
import { Core } from "@/sections/Core"
import { Explode } from "@/sections/Explode"
import { Family, Products } from "@/sections/Products"
import { AI, Partner, CTA } from "@/sections/Closing"
import { Faq } from "@/sections/Faq"

function Page() {
  useBreathingLight()
  return (
    <>
      <Nav />
      <main>
        <Hero />
        <Core />
        <Explode />
        <Family />
        <Products />
        <AI />
        <Partner />
        <Faq />
        <CTA />
      </main>
    </>
  )
}

export default function App() {
  return (
    <MotionConfig reducedMotion="user">
      <AppProvider>
        <TooltipProvider delayDuration={150}>
          <Page />
        </TooltipProvider>
      </AppProvider>
    </MotionConfig>
  )
}
