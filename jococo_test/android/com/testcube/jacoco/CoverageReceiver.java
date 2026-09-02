package com.testcube.jacoco;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.util.Log;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;

/**
 * Writes JaCoCo execution data when TestCube / JacocoBridge sends a broadcast.
 *
 * Action must stay in sync with JacocoBridge:
 *   com.llmdroid.jacoco.COLLECT_COVERAGE
 *
 * Extra:
 *   coverageFile — filename under getExternalFilesDir(null)
 */
public class CoverageReceiver extends BroadcastReceiver {

    private static final String TAG = "CoverageReceiver";
    public static final String ACTION = "com.llmdroid.jacoco.COLLECT_COVERAGE";
    public static final String EXTRA_FILE = "coverageFile";

    @Override
    public void onReceive(Context context, Intent intent) {
        if (intent == null || !ACTION.equals(intent.getAction())) {
            return;
        }
        String fileName = intent.getStringExtra(EXTRA_FILE);
        if (fileName == null || fileName.trim().isEmpty()) {
            fileName = "coverage.ec";
        }
        File dir = context.getExternalFilesDir(null);
        if (dir == null) {
            Log.e(TAG, "External files dir unavailable");
            return;
        }
        if (!dir.exists() && !dir.mkdirs()) {
            Log.e(TAG, "Could not create " + dir);
            return;
        }
        File target = new File(dir, fileName);
        OutputStream out = null;
        try {
            out = new FileOutputStream(target, false);
            Object agent = Class.forName("org.jacoco.agent.rt.RT")
                    .getMethod("getAgent")
                    .invoke(null);
            byte[] data = (byte[]) agent.getClass()
                    .getMethod("getExecutionData", boolean.class)
                    .invoke(agent, true);
            out.write(data);
            Log.i(TAG, "Wrote coverage to " + target.getAbsolutePath());
        } catch (Exception exc) {
            Log.e(TAG, "Coverage dump failed: " + exc, exc);
        } finally {
            if (out != null) {
                try {
                    out.close();
                } catch (IOException ignored) {
                }
            }
        }
    }
}
